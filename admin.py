from sqladmin import Admin, ModelView
from database import engine, SessionLocal
from models import User, Movie, Review
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from passlib.context import CryptContext
from logger import logger

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")
        db_session = SessionLocal()

        user = db_session.query(User).filter(User.username == username).first()
        print(f"User found: {user}")

        if user and pwd_context.verify(password, user.hashed_password):
            if user.is_admin:
                logger.info(f"Admin login successful: {username}")
                request.session.update({"token": user.username})
                return True
            else:
                logger.warning(f"Unauthorized login attempt by non-admin: {username}")
                return False
        else:
            logger.warning(f"Failed login attempt: {username}")
            return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        return token is not None

class UsersAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.is_admin]
        
class MovieAdmin(ModelView, model=Movie):
    column_list = [Movie.id, Movie.title, Movie.genre, Movie.year, 'user', 'category', 'reviews']

class ReviewsAdmin(ModelView, model=Review):
    column_list = [Review.id, Review.comment, Review.rating, 'user', 'movie']
    name = "Review"
    name_plural = "Reviews"
    icon = "fa-solid fa-star"

def create_admin(app):
    authentication_backend = AdminAuth(secret_key="supersecretkey")
    admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)
    admin.add_view(UsersAdmin)
    admin.add_view(MovieAdmin)
    admin.add_view(ReviewsAdmin)
    return admin
