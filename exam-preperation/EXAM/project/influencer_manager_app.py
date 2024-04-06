from typing import List
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer



class InfluencerManagerApp:
    TYPE_INFLUENCER = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    TYPE_CAMPAIGN = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}


    def __init__(self) -> None:
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []


    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.TYPE_INFLUENCER:
            return f"{influencer_type} is not an allowed influencer type."
        
        if self.find_influencer_by_name(username):
            return f"{username} is already registered."
        
        new_infuencer = self.TYPE_INFLUENCER[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_infuencer)
        return f"{username} is successfully registered as a {influencer_type}."


    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.TYPE_CAMPAIGN:
            return f"{campaign_type} is not a valid campaign type."
        
        if self.find_campaign_by_id(campaign_id):
            return f"Campaign ID {campaign_id} has already been created."
        
        new_campaign = self.TYPE_CAMPAIGN[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."


    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self.find_influencer_by_name(influencer_username)
        campaign = self.find_campaign_by_id(campaign_id)

        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."
        
        payment = influencer.calculate_payment(campaign)
        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

        return ""



    def calculate_total_reached_followers(self):
        total_reached_followers = {}
        for campaign in self.campaigns:
            reached_followers = 0
            for influencer in campaign.approved_influencers:
                reached_followers += influencer.reached_followers(type(campaign).__name__)
            if reached_followers > 0:
                total_reached_followers[campaign] = reached_followers
        return total_reached_followers


    def influencer_campaign_report(self, username: str):
        influencer = self.find_influencer_by_name(username)
        campaign_report = influencer.display_campaigns_participated()
        
        # if not influencer or not campaign_report:
        #     return f"{username} has not participated in any campaigns."

        # return f"{type(influencer).__name__} :) {username} :) participated in the following campaigns:\n\n{campaign_report}\n"
        return campaign_report


    def campaign_statistics(self):
    # Sort campaigns by the total number of approved influencers, ascending
        sorted_campaigns = sorted(self.campaigns, key=lambda campaign: (len(campaign.approved_influencers), -campaign.budget))

        # Generate the campaign statistics report
        report = "$$ Campaign Statistics $$\n"
        for campaign in sorted_campaigns:
            total_reached_followers = sum(influencer.reached_followers(campaign.__class__.__name__) for influencer in campaign.approved_influencers)
            report += f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}\n"

        return report



    #helper method
    def find_influencer_by_name(self, influencer_name):
        for influencer in self.influencers:
            if influencer.username == influencer_name:
                return influencer
        return None
    

    def find_campaign_by_id(self, campaign_id):
        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return campaign
        return None