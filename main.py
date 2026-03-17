from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from content_factory.api.routes import router

app = FastAPI()

# CORS setup for frontend integration
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],  # Adjust for production
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(router)
