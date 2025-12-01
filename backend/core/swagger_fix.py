# core/swagger_fix.py
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema

class FixDuplicateSchema(SwaggerAutoSchema):
    def get_responses(self):
        responses = super().get_responses()
        
        # Solo para métodos que tienen request body
        if self.method.lower() in ['post', 'put', 'patch']:
            for code, response in responses.items():
                # Mantenemos los schemas para códigos de error y respuestas personalizadas
                if code in ['200', '201', '204']:
                    # Para códigos de éxito, mostramos solo la descripción sin schema duplicado
                    if hasattr(response, 'schema') and response.schema:
                        # Solo mantenemos schema si es diferente al request
                        response.schema = None
                # Para códigos de error (400, 401, 403, 404, 500) mantenemos los schemas
                # Para que se muestren los formatos de error
                
        return responses

    def get_operation(self, operation_keys):
        operation = super().get_operation(operation_keys)
        
        # Mejorar las descripciones automáticamente
        if not operation.description:
            if self.method.lower() == 'get':
                operation.description = "Retrieve data"
            elif self.method.lower() == 'post':
                operation.description = "Create new resource"  
            elif self.method.lower() == 'put':
                operation.description = "Update resource"
            elif self.method.lower() == 'delete':
                operation.description = "Delete resource"
                
        return operation