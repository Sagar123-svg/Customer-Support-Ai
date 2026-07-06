documents = {
    "Billing": {
        "file": "refund_policy.txt",
        "content": open(
            "knowledge_base/refund_policy.txt",
            "r",
            encoding="utf-8"
        ).read()
    },

    "Shipping": {
        "file": "shipping_policy.txt",
        "content": open(
            "knowledge_base/shipping_policy.txt",
            "r",
            encoding="utf-8"
        ).read()
    },

    "Technical": {
        "file": "technical_faq.txt",
        "content": open(
            "knowledge_base/technical_faq.txt",
            "r",
            encoding="utf-8"
        ).read()
    }
}


def retrieve_document(category):
    return documents.get(category)