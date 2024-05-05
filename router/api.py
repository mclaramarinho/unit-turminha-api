from fastapi import APIRouter

from router.event_routes import router as event_router
from router.faq_routes import router as faq_router
from router.class_routes import router as class_router
from router.contact_routes import router as contact_router
from router.admin_routes import router as admin_router
from router.code_routes import router as code_router


router = APIRouter()

router.include_router(event_router, tags=["events"], prefix="/api/events")
router.include_router(faq_router, tags=["faq", 'frequently asked questions'], prefix="/api/faq")
router.include_router(class_router, tags=["class"], prefix="/api/class")
router.include_router(contact_router, tags=['contact'], prefix="/api/contact")
router.include_router(admin_router, tags=['admin'], prefix="/api/admin")
router.include_router(code_router, tags=["code"], prefix="/api/code")