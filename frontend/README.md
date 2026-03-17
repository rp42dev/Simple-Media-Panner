This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/pages/api-reference/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `pages/index.js`. The page auto-updates as you edit the file.

## Agent Selection Feature

This UI allows users to select which agents (SEO, analytics, video, carousel) to include when generating monthly content. Agent outputs are displayed for each content item.

### Usage
1. Enter a topic and number of posts per month.
2. Select desired agents using the checkboxes.
3. Click "Generate Content".
4. Agent outputs (SEO, analytics, video, carousel) will appear under each content item if selected.

### Example
- SEO: Shows optimized content and meta.
- Analytics: Shows stub views and engagement.
- Video: Shows stub script and meta.
- Carousel: Shows stub slide(s).

### API Integration
The frontend sends agent selection fields to the backend:
- `include_seo`, `include_analytics`, `include_video`, `include_carousel`

### Screenshots
(Add screenshots after running the app)

---

For backend setup and API details, see the main project README.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn-pages-router) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/pages/building-your-application/deploying) for more details.
