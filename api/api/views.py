from djoser.views import TokenCreateView


class CustomTokenCreateView(TokenCreateView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Retrieve the user ID from the authenticated user object
        user_id = self.request.user.id

        # Include the user ID in the response data
        response.data['user_id'] = user_id

        return response
