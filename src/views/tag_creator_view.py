from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController


class TagCreatorView:

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body['product_code']

        if product_code is None:
            return HttpResponse(
                status_code=400,
                body={'message': 'Product code is required!'}
                )

        formatted_response = tag_creator_controller.create(product_code)

        return HttpResponse(
            status_code=200,
            body=formatted_response
            )
