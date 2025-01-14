from .database import db

class Influencer(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)
    name = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False)
    category = db.Column(db.String(), nullable = False)
    reach = db.Column(db.String(), nullable = False)
    description = db.Column(db.Text(), nullable = False)
    flag_status = db.Column(db.String(), default = "Unflagged") # Unflagged / Flagged

class Sponsor(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)
    name = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(), nullable = False)
    industry = db.Column(db.String(), nullable = False)
    budget = db.Column(db.String(), nullable = False)
    description = db.Column(db.Text(), nullable = False)
    flag_status = db.Column(db.String(), default = "Unflagged") # Unflagged / Flagged
    campaigns = db.relationship("Campaign", backref = "sponsor")

class Campaign(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(), nullable = False)
    start_date = db.Column(db.String(), nullable = False)
    end_date = db.Column(db.String(), nullable = False)
    budget = db.Column(db.Float(), nullable = False)
    visibility = db.Column(db.String(), nullable = False) # Public / Private
    target = db.Column(db.String(), nullable = False)
    status = db.Column(db.String(), default = "Active") # Active / Over
    description = db.Column(db.Text(), nullable = False)
    flag_status = db.Column(db.String(), default = "Unflagged") # Unflagged / Flagged
    sponsor_id = db.Column(db.Integer(), db.ForeignKey('sponsor.id'), nullable = False)
    ad_requests = db.relationship("AdRequest", backref = "campaign")

class AdRequest(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    campaign_id = db.Column(db.Integer(), db.ForeignKey('campaign.id'), nullable = False)
    influencer_id = db.Column(db.Integer(), db.ForeignKey('influencer.id'), nullable = False)
    message = db.Column(db.Text(), nullable = False)
    requirements = db.Column(db.Text(), nullable = False)
    payment_amount = db.Column(db.Float(), nullable = False)
    status = db.Column(db.String(), default = "Pending") # Pending / Accepted / Rejected
    owner = db.Column(db.String(), nullable = False) # Influencer / Sponsor
    influencer_work_status = db.Column(db.String(), default = "0%") # 0% / 25% / 50% / 75% / 100% / Confirmation Pending / Payment Pending / Payment Recieved
    influencer = db.relationship("Influencer", backref="ad_requests")