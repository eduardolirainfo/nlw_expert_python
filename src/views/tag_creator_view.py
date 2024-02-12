from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class TagCreatorView:

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body['product_code']

        if product_code is None:
            return HttpResponse(
                status_code=400,
                body={'message': 'Product code is required!'}
                )
        print(f'Creating tag for product code: {product_code}')

        return HttpResponse(
            status_code=200,
            body={'message': 'Tag created successfully!'}
            )
