from schema import Schema

schema = Schema(
    {
        "userId": str,
        "paymentMethod": str,
        "total": str,
        "pizzas": [{"id": str, "name": str, "price": str}],
        "requestedAtDate": str,
        "requestedAtTime": str,
        "processedAtDate": str,
        "processedAtTime": str,
        "status": str,
        "id": str,
    }
)


def validate(event):
    return schema.validate(event)
