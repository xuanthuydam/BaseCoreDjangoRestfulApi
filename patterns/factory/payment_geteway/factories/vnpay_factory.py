from patterns.factory.payment_geteway.base import PaymentGatewayFactory
from patterns.factory.payment_geteway.payment_gateways.vnpay_gateway import \
    VNPayGateway


class VNPayGatewayFactory(PaymentGatewayFactory):
    def create_payment_gateway(self, *arg, **kwargs):
        return VNPayGateway()
