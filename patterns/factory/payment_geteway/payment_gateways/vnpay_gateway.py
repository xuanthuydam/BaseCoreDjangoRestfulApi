from patterns.factory.payment_geteway.base import PaymentGateway


class VNPayGateway(PaymentGateway):
    def initiate_payment(self, *arg, **kwargs):
        return "VNPay Initiate Payment"

    def verify_payment(self, *arg, **kwargs):
        return "VNPay Verify Payment"

    def refund_payment(self, *arg, **kwargs):
        return "VNPay Refund Payment"

    def cancel_payment(self, *arg, **kwargs):
        return "VNPay Cancel Payment"

    def get_payment_status(self, *arg, **kwargs):
        return "VNPay Get Payment Status"
