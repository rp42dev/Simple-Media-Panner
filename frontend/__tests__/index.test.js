import '@testing-library/jest-dom';
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Home from '../components/Home';

jest.mock('axios', () => ({
  get: jest.fn(() => Promise.resolve({ data: { agents: {
    seo: { enabled: true },
    analytics: { enabled: false },
    video: { enabled: false },
    carousel: { enabled: false }
  } } })),
  post: jest.fn((url, payload) => {
    // Simulate backend response
    const agentKeys = ['seo', 'analytics', 'video', 'carousel'];
    const content = [
      {
        topic: payload.topic,
        category: 'Test Category',
        tone: 'Test Tone',
        content: 'Test Content',
        visuals: 'Test Visuals',
        ...(payload.include_seo ? { seo: 'stub' } : {}),
        ...(payload.include_analytics ? { analytics: 'stub' } : {}),
        ...(payload.include_video ? { video: 'stub' } : {}),
        ...(payload.include_carousel ? { carousel: 'stub' } : {}),
      }
    ];
    return Promise.resolve({ data: { monthly_content: content } });
  })
}));

describe('Home page agent selection', () => {
  beforeAll(() => {
    window.alert = jest.fn();
  });
  it('renders agent checkboxes and displays outputs', async () => {
    render(<Home />);
    screen.getByText('Dental Content Generator');
    fireEvent.change(screen.getByPlaceholderText('Enter topic'), { target: { value: 'Test' } });
    const seoCheckbox = await screen.findByRole('checkbox', { name: /seo/i });
    fireEvent.click(seoCheckbox);
    fireEvent.click(screen.getByText('Generate Content'));
    // Wait for async content and SEO Output heading
    await screen.findByText('"Test Content"');
    await screen.findByText('SEO Output');
    // Debug output
    // eslint-disable-next-line no-console
    // @ts-ignore
    // eslint-disable-next-line testing-library/no-debugging-utils
    screen.debug();
    expect(screen.queryByText('SEO Output')).toBeInTheDocument();
  });

  it('shows error popup on backend error', async () => {
    jest.spyOn(require('axios'), 'post').mockImplementationOnce(() => Promise.reject());
    render(<Home />);
    fireEvent.change(screen.getByPlaceholderText('Enter topic'), { target: { value: 'Test' } });
    fireEvent.click(screen.getByText('Generate Content'));
    // Wait for alert to be called
    await Promise.resolve();
    expect(window.alert).toHaveBeenCalledWith('Error generating content');
  });
});
