from rest_framework.permissions import BasePermission


class GenrePersmissionsClass(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')

        if request.method in 'POST':
            return request.user.has_perm('genres.add_genre')

        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('genres.change_genre')

        if request.method in 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        
        return False
