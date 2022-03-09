from apps.users.views import users
from apps.main.views import index


urlpatterns = {
    '/': index,
    '/users/': users,
}
