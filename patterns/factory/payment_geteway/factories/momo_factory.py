from patterns.factory.payment_geteway.base import PaymentGatewayFactory
from patterns.factory.payment_geteway.payment_gateways.momo_gateway import \
    MoMoGateway


class MoMoGatewayFactory(PaymentGatewayFactory):
    def create_payment_gateway(self, *arg, **kwargs):
        return MoMoGateway()
