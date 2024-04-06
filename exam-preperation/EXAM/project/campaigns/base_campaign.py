from abc import ABC, abstractmethod


class BaseCampaign(ABC):

    _unique_campaign_ids = set()

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float) -> None:
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers = []

        self._unique_campaign_ids.add(campaign_id)


    @property
    def campaign_id(self):
        return self.__campaign_id
    
    @campaign_id.setter
    def campaign_id(self, value):
        if value < 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")
        self.__campaign_id = value


    @abstractmethod
    def check_eligibility(self, engagement_rate: float):
        pass