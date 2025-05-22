from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(self, *arg, **kwargs):
        pass

    @abstractmethod
    def verify_payment(self, *arg, **kwargs):
        pass

    @abstractmethod
    def refund_payment(self, *arg, **kwargs):
        pass

    @abstractmethod
    def cancel_payment(self, *arg, **kwargs):
        pass

    @abstractmethod
    def get_payment_status(self, *arg, **kwargs):
        pass


class PaymentGatewayFactory(ABC):
    @abstractmethod
    def create_payment_gateway(self, *arg, **kwargs):
        pass
