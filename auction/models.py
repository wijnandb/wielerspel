from django.contrib.auth.models import User
from django.db import models
from results.models import Rider


class TeamCaptain(models.Model):
    """ 
    Information about the TeamCaptains: how many riders have they bought,
    how much points do they have left, what is max. bid, how many riders 
    do they still need to buy?
    """
    name = models.CharField(max_length=30, default='naam invoeren')
    team_size = models.IntegerField(default=0)
    amount_left = models.IntegerField(default=100)
    riders_needed = models.IntegerField(default=9)
    max_allowed_bid = models.IntegerField(default=92)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-amount_left', '-name']


class Bid(models.Model):
    """
    The bidding. Who bids how much for whom?
    """
    team_captain = models.ForeignKey(User, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='rider')
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s - %s" %(self.team_captain.name, self.rider.name, self.amount)



class ToBeAuctioned(models.Model):
    """
    The wishlist for each Teamcaptain. A rider can be on the wishlist of 
    multiple TeamCaptains. Once a rider is auctioned, it is removed from 
    everyone's wishlist.
    """
    team_captain = models.ForeignKey(User, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    #on_auction = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "%s biedt %s aan voor %s" %(self.team_captain, self.rider.name, self.amount)


class AuctionOrder(models.Model):
    """
    We need to determine the order in which riders are being auctioned.
    The TeamCaptains take turns proposing a rider to be auctioned.
    After each auctioned rider, the order has to be changed: number 1
    teamcaptain shifts to last order (count(teamcaptains)+1) and then each
    order goes -1: order = order -1
    Once a TeamCaptain doesn't have anymore points to spend, he gets 
    taken of the list.
    """
    team_captain = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.IntegerField()


class Joker(models.Model):
    """
    TeamCaptains can have a "Joker" placed on three riders they have had in
    previous year(s). This allows them to buy that Rider for a lower amount than 
    the other TeamCaptains. A Joker with a value of 0 allows them to buy the
    rider for the highest amount the other TeamCaptains have bidded.
    """
    team_captain = models.ForeignKey(User, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    def __str__(self):
        return "%s heeft een %s joker op %s" %(self.team_captain, self.value, self.rider.name)


class VirtualTeam(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    ploegleider = models.ForeignKey(User, on_delete=models.CASCADE)
    editie = models.PositiveIntegerField(default=2021)
    price = models.IntegerField(default=0)
    punten = models.FloatField(default=0)
    jpp = models.IntegerField(default=0)

    unique_together = [['rider', 'editie']]

    class Meta:
        ordering = ['-price']
        verbose_name_plural = 'Sold riders'

    def __str__(self):
        return "%s - %s -%s" %(self.rider, self.price, self.ploegleider)
