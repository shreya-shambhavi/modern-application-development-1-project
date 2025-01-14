from flask import Flask, render_template, redirect, request
from flask import current_app as app
from .models import *

# Home Page Of The Application
@app.route("/", methods = ['GET', 'POST'])
def home_page():
    return render_template("index.html")

# ADMIN ROUTES--------------------------------------------------------------------------------------------

# Admin Login [Page]
@app.route("/admin_login", methods = ['GET', 'POST'])
def admin_login():
    if request.method == "POST":
        admin_username = request.form.get("admin_username")
        admin_password = request.form.get("admin_password")

        if admin_username == "Admin" and admin_password == "1234567890":
            return redirect("/admin_dashboard")
        else:
            return "Invalid Admin Credentials"
        
    return render_template("admin_login.html")

# Admin Dashboard [Page]
@app.route("/admin_dashboard", methods = ['GET', 'POST'])
def admin_dashboard():
    return render_template("admin_dashboard.html")

# Admin All Campaigns [Page]
@app.route("/all_campaigns", methods = ['GET', 'POST'])
def all_campaigns():
    all_campaigns = Campaign.query.all()

    return render_template("admin_all_campaigns.html", all_campaigns = all_campaigns)

# Admin View Campaign [Button]
@app.route("/admin_view_campaign/<int:campaign_id>", methods = ['GET', 'POST'])
def admin_view_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    all_adrequests = AdRequest.query.filter_by(campaign_id = campaign_id).all()

    return render_template("admin_view_campaign.html", campaign = campaign, all_adrequests = all_adrequests)

# Admin Flag Campaign [Button]
@app.route("/flag_campaign/<int:campaign_id>", methods = ['POST'])
def flag_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    campaign.flag_status = "Flagged"

    db.session.commit()

    return redirect("/flagged_campaigns")

# Admin Unflag Campaign [Button]
@app.route("/unflag_campaign/<int:campaign_id>", methods = ['POST'])
def unflag_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    campaign.flag_status = "Unflagged"

    db.session.commit()

    return redirect("/all_campaigns")

# Admin All Influencers [Page]
@app.route("/all_influencers", methods = ['GET', 'POST'])
def all_influencers():
    all_influencers = Influencer.query.all()

    return render_template("admin_all_influencers.html", all_influencers = all_influencers)

# Admin View Influencer [Button]
@app.route("/admin_view_influencer/<int:influencer_id>", methods = ['GET', 'POST'])
def admin_view_influencer(influencer_id):
    influencer = Influencer.query.get(influencer_id)
    all_adrequests = AdRequest.query.filter_by(influencer_id = influencer_id).all()

    return render_template("admin_view_influencer.html", influencer = influencer, all_adrequests = all_adrequests)

# Admin Flag Influencer [Button]
@app.route("/flag_influencer/<int:influencer_id>", methods = ['POST'])
def flag_influencer(influencer_id):
    influencer = Influencer.query.get(influencer_id)
    influencer.flag_status = "Flagged"

    db.session.commit()

    return redirect("/flagged_influencers")

# Admin Unflag Influencer [Button]
@app.route("/unflag_influencer/<int:influencer_id>", methods = ['POST'])
def unflag_influencer(influencer_id):
    influencer = Influencer.query.get(influencer_id)
    influencer.flag_status = "Unflagged"

    db.session.commit()

    return redirect("/all_influencers")

# Admin All Sponsors [Page]
@app.route("/all_sponsors", methods = ['GET', 'POST'])
def all_sponsors():
    all_sponsors = Sponsor.query.all()

    return render_template("admin_all_sponsors.html", all_sponsors = all_sponsors)

# Admin View Sponsor [Button]
@app.route("/admin_view_sponsor/<int:sponsor_id>", methods = ['GET', 'POST'])
def admin_view_sponsor(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)
    all_campaigns = Campaign.query.filter_by(sponsor_id = sponsor_id).all()

    return render_template("admin_view_sponsor.html", sponsor = sponsor, all_campaigns = all_campaigns)

# Admin Flag Sponsor [Button]
@app.route("/flag_sponsor/<int:sponsor_id>", methods = ['POST'])
def flag_sponsor(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)
    sponsor.flag_status = "Flagged"

    db.session.commit()

    return redirect("/flagged_sponsors")

# Admin Unflag Sponsor [Button]
@app.route("/unflag_sponsor/<int:sponsor_id>", methods = ['POST'])
def unflag_sponsor(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)
    sponsor.flag_status = "Unflagged"

    db.session.commit()

    return redirect("/all_sponsors")

# Admin Flagged Campaigns [Page]
@app.route("/flagged_campaigns", methods = ['GET', 'POST'])
def flagged_campaigns():
    flagged_campaigns = Campaign.query.filter_by(flag_status = "Flagged").all()
    
    return render_template("admin_flagged_campaigns.html", flagged_campaigns = flagged_campaigns)

# Admin View Flagged Campaign [Button]
@app.route("/admin_view_flagged_campaign/<int:campaign_id>", methods = ['GET', 'POST'])
def admin_view_flagged_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    all_adrequests = AdRequest.query.filter_by(campaign_id = campaign_id).all()

    return render_template("admin_view_flagged_campaign.html", campaign = campaign, all_adrequests = all_adrequests)

# Admin Remove a Flagged Campaign [Button]
@app.route("/admin_remove_flagged_campaign/<int:campaign_id>", methods = ['POST'])
def admin_remove_flagged_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)

    if campaign:
        db.session.query(AdRequest).filter_by(campaign_id = campaign_id).delete()
        db.session.delete(campaign)
        db.session.commit()

    return redirect("/flagged_campaigns")

# Admin Flagged Influencers [Page]
@app.route("/flagged_influencers", methods = ['GET', 'POST'])
def flagged_influencers():
    flagged_influencers = Influencer.query.filter_by(flag_status = "Flagged").all()

    return render_template("admin_flagged_influencers.html", flagged_influencers = flagged_influencers)

# Admin View Flagged Influencer [Button]
@app.route("/admin_view_flagged_influencer/<int:influencer_id>", methods = ['GET', 'POST'])
def admin_view_flagged_influencer(influencer_id):
    influencer = Influencer.query.get(influencer_id)
    all_adrequests = AdRequest.query.filter_by(influencer_id = influencer_id).all()

    return render_template("admin_view_flagged_influencer.html", influencer = influencer, all_adrequests = all_adrequests)

# Admin Remove a Flagged Influencer [Button]
@app.route("/admin_remove_flagged_influencer/<int:influencer_id>", methods = ['POST'])
def admin_remove_flagged_influencer(influencer_id):
    influencer = Influencer.query.get(influencer_id)

    if influencer:
        db.session.query(AdRequest).filter_by(influencer_id = influencer_id).delete()
        db.session.delete(influencer)
        db.session.commit()

    return redirect("/flagged_influencers")

# Admin Flagged Sponsors [Page]
@app.route("/flagged_sponsors", methods = ['GET', 'POST'])
def flagged_sponsors():
    flagged_sponsors = Sponsor.query.filter_by(flag_status = "Flagged").all()

    return render_template("admin_flagged_sponsors.html", flagged_sponsors = flagged_sponsors)

# Admin View Flagged Sponsor [Button]
@app.route("/admin_view_flagged_sponsor/<int:sponsor_id>", methods = ['GET', 'POST'])
def admin_view_flagged_sponsor(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)
    all_campaigns = Campaign.query.filter_by(sponsor_id = sponsor_id).all()

    return render_template("admin_view_flagged_sponsor.html", sponsor = sponsor, all_campaigns = all_campaigns)

# Admin Remove a Flagged Sponsor [Button]
@app.route("/admin_remove_flagged_sponsor/<int:sponsor_id>", methods = ['POST'])
def admin_remove_flagged_sponsor(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)

    if sponsor:
        for campaign in sponsor.campaigns:
            db.session.query(AdRequest).filter_by(campaign_id = campaign.id).delete()

        db.session.query(Campaign).filter_by(sponsor_id = sponsor_id).delete()
        db.session.delete(sponsor)
        db.session.commit()

    return redirect("/flagged_sponsors")

# Admin Platform Statistics [Page]
@app.route("/admin_dashboard_statistics", methods = ['GET', 'POST'])
def admin_dashboard_statistics():
    total_sponsors = Sponsor.query.count()
    total_influencers = Influencer.query.count()
    active_campaigns = Campaign.query.filter_by(status = "Active").count()
    active_public_campaigns = Campaign.query.filter_by(status = "Active", visibility = "Public").count()
    active_private_campaigns = Campaign.query.filter_by(status = "Active", visibility = "Private").count()
    total_adrequests = AdRequest.query.count()
    total_pending_adrequests = AdRequest.query.filter_by(status = "Pending").count()
    total_accepted_adrequests = AdRequest.query.filter_by(status = "Accepted").count()
    total_rejected_adrequests = AdRequest.query.filter_by(status = "Rejected").count()
    total_flagged_sponsors = Sponsor.query.filter_by(flag_status = "Flagged").count()
    total_flagged_influencers = Influencer.query.filter_by(flag_status = "Flagged").count()
    total_flagged_campaigns = Campaign.query.filter_by(flag_status = "Flagged").count()
    adrequest_sent_by_sponsor = AdRequest.query.filter_by(owner = "Sponsor").count()
    adrequest_sent_by_influencer = AdRequest.query.filter_by(owner = "Influencer").count()
    completed_campaigns = Campaign.query.filter_by(status = "Over").count()

    return render_template("admin_dashboard_statistics.html", total_sponsors = total_sponsors, total_influencers = total_influencers, active_campaigns = active_campaigns, active_public_campaigns = active_public_campaigns, active_private_campaigns = active_private_campaigns, total_adrequests = total_adrequests, total_pending_adrequests = total_pending_adrequests, total_accepted_adrequests = total_accepted_adrequests, total_rejected_adrequests = total_rejected_adrequests, total_flagged_sponsors = total_flagged_sponsors, total_flagged_influencers = total_flagged_influencers, total_flagged_campaigns = total_flagged_campaigns, adrequest_sent_by_sponsor = adrequest_sent_by_sponsor, adrequest_sent_by_influencer = adrequest_sent_by_influencer, completed_campaigns = completed_campaigns)

# INFLUENCER ROUTES---------------------------------------------------------------------------------------

# Influencer Registration [Page]
@app.route("/influencer_registration", methods = ['GET', 'POST'])
def influencer_registration():
    if request.method == "POST":
        influencer_username = request.form.get("influencer_username")
        influencer_password = request.form.get("influencer_password")
        influencer_name = request.form.get("influencer_name")
        influencer_email = request.form.get("influencer_email")
        influencer_category = request.form.get("influencer_category")
        influencer_reach = request.form.get("influencer_reach")
        influencer_description = request.form.get("influencer_description")
        this_influencer = Influencer.query.filter_by(username = influencer_username).first()

        if this_influencer:
            return "Username already exists!"
        else:
            new_influencer = Influencer(username = influencer_username, password = influencer_password, name = influencer_name, email = influencer_email, category = influencer_category, reach = influencer_reach, description = influencer_description)

            db.session.add(new_influencer)
            db.session.commit()
            return redirect("/influencer_login")

    return render_template("influencer_registration.html")

# Influencer Login [Page]
@app.route("/influencer_login", methods = ['GET', 'POST'])
def influencer_login():
    if request.method == "POST":
        influencer_username = request.form.get("influencer_username")
        influencer_password = request.form.get("influencer_password")
        this_influencer = Influencer.query.filter_by(username = influencer_username).first()

        if this_influencer:
            if this_influencer.password == influencer_password:
                return redirect(f'/influencer_dashboard/{this_influencer.id}')
            else:
                return "Incorrect Password"
        else:
            return "User doesn't exist. Kindly Register first to login."
        
    return render_template("influencer_login.html")

# Influencer Dashboard [Page]
@app.route("/influencer_dashboard/<int:influencer_id>", methods = ['GET', 'POST'])
def influencer_dashboard(influencer_id):
    influencer = Influencer.query.get(influencer_id)

    return render_template("influencer_dashboard.html", influencer = influencer)

# Influencer Profile [Page]
@app.route("/influencer_profile_page/<int:influencer_id>", methods = ['GET', 'POST'])
def influencer_profile_page(influencer_id):
    influencer = Influencer.query.get(influencer_id)

    payment_recieved = AdRequest.query.filter_by(influencer_id = influencer_id, status = "Accepted", influencer_work_status = "Payment Recieved").all()
    total_earning = sum(adrequest.payment_amount for adrequest in payment_recieved)

    return render_template("influencer_profile_page.html", influencer = influencer, total_earning = total_earning)

# Influencer Update Profile [Button]
@app.route("/influencer_update_profile/<int:influencer_id>", methods = ['GET', 'POST'])
def influencer_update_profile(influencer_id):
    influencer = Influencer.query.get(influencer_id)

    if request.method == "POST":
        influencer.username = request.form.get("influencer_username")
        influencer.password = request.form.get("influencer_password")
        influencer.name = request.form.get("influencer_name")
        influencer.email = request.form.get("influencer_email")
        influencer.category = request.form.get("influencer_category")
        influencer.reach = request.form.get("influencer_reach")
        influencer.description = request.form.get("influencer_description")
    
        db.session.commit()

        return redirect(f'/influencer_profile_page/{influencer.id}')

    return render_template("influencer_update_profile.html", influencer = influencer)

# Influencer Delete Account [Button]
@app.route("/delete_influencer_account/<int:influencer_id>", methods = ['POST'])
def delete_influencer_account(influencer_id):
    influencer = Influencer.query.get(influencer_id)

    if influencer:
        db.session.query(AdRequest).filter_by(influencer_id = influencer_id).delete()
        db.session.delete(influencer)
        db.session.commit()

    return redirect("/")

# Influencer My Work [Page]
@app.route("/influencer_myworks/<int:influencer_id>", methods = ['GET', 'POST'])
def influencer_myworks(influencer_id):
    influencer = Influencer.query.get(influencer_id)
    accepted_adrequests = AdRequest.query.filter_by(influencer_id = influencer_id, status = "Accepted").all()

    return render_template("influencer_my_works.html", influencer = influencer, accepted_adrequests = accepted_adrequests)

# Influencer Update Work Status [Button]
@app.route("/influencer_update_work_status/<int:influencer_id>/<int:adrequest_id>", methods = ['POST'])
def influencer_update_work_status(influencer_id, adrequest_id):
    influencer = Influencer.query.get(influencer_id)
    adrequest = AdRequest.query.get(adrequest_id)

    if adrequest:
        if adrequest.influencer_work_status == "0%":
            adrequest.influencer_work_status = "25%"
        elif adrequest.influencer_work_status == "25%":
            adrequest.influencer_work_status = "50%"
        elif adrequest.influencer_work_status == "50%":
            adrequest.influencer_work_status = "75%"
        elif adrequest.influencer_work_status == "75%":
            adrequest.influencer_work_status = "100%"
        elif adrequest.influencer_work_status == "100%":
            adrequest.influencer_work_status = "Confirmation Pending"
        
        db.session.commit()
    
    return redirect(f'/influencer_myworks/{influencer.id}')

# Influencer View Work [Button]
@app.route("/influencer_view_work/<int:influencer_id>/<int:adrequest_id>", methods = ['GET', 'POST'])
def influencer_view_work(influencer_id,adrequest_id):
    influencer = Influencer.query.get(influencer_id)
    adrequest = AdRequest.query.get(adrequest_id)

    return render_template("influencer_view_work.html", influencer = influencer, adrequest = adrequest)

# Influencer Find a Campaign [Page]
@app.route("/public_campaigns/<int:influencer_id>", methods = ['GET', 'POST'])
def influencer_public_campaigns(influencer_id):
    influencer = Influencer.query.get(influencer_id)
    public_campaigns = Campaign.query.filter_by(visibility = "Public").all()
    
    return render_template("influencer_public_campaigns.html", influencer = influencer, public_campaigns = public_campaigns)

# Influencer Search Campaigns [Page]
@app.route("/influencer_search_campaigns/<int:influencer_id>", methods = ['GET', 'POST'])
def influencer_search_campaigns(influencer_id):
    
    influencer = Influencer.query.get(influencer_id)

    if request.method == "POST":
        search_word = request.form.get("search_word")
        return redirect(f'/influencer_search_campaigns/{influencer.id}?search_word={search_word}')

    search_word = request.args.get('search_word', '')
    
    if search_word:
        search = f"%{search_word}%"
        name_results = Campaign.query.filter(Campaign.name.like(search)).all()
        start_date_results = Campaign.query.filter(Campaign.start_date.like(search)).all()
        end_date_results = Campaign.query.filter(Campaign.end_date.like(search)).all()
        target_results = Campaign.query.filter(Campaign.target.like(search)).all()
        result_campaigns = name_results + target_results + start_date_results + end_date_results
    else:
        result_campaigns = []

    return render_template("influencer_search_campaigns.html", influencer = influencer, result_campaigns = result_campaigns, search_word = search_word)

# Influencer View Public Campaign [Button]
@app.route("/influencer_view_public_campaign/<int:influencer_id>/<int:campaign_id>", methods = ['GET', 'POST'])
def influencer_view_public_campaign(influencer_id,campaign_id):
    influencer = Influencer.query.get(influencer_id)
    campaign = Campaign.query.get(campaign_id)
    adrequests = AdRequest.query.filter_by(campaign_id = campaign_id).all()

    return render_template("influencer_view_public_campaign.html", influencer = influencer, campaign = campaign, adrequests = adrequests)

# Influencer Create An Ad Request [Button]
@app.route("/influencer_create_adrequest/<int:influencer_id>/<int:campaign_id>", methods = ['GET', 'POST'])
def influencer_create_adrequest(influencer_id, campaign_id):
    influencer = Influencer.query.get(influencer_id)
    campaign = Campaign.query.get(campaign_id)

    if request.method == "POST":
        adrequest_message = request.form.get("adrequest_message")
        adrequest_requirements = request.form.get("adrequest_requirements")
        adrequest_payment_amount = request.form.get("adrequest_payment_amount")
        adrequest_owner = "Influencer"

        new_adrequest = AdRequest(message = adrequest_message, requirements = adrequest_requirements, payment_amount = adrequest_payment_amount, owner = adrequest_owner, campaign_id = campaign.id, influencer_id = influencer.id)
        db.session.add(new_adrequest)
        db.session.commit()
        return redirect(f'/influencer_adrequests_sent/{influencer.id}')

    return render_template("influencer_create_adrequest.html", influencer = influencer, campaign = campaign)

# Influencer New Ad Requests Recieved [Page]
@app.route("/influencer_adrequests_recieved/<int:influencer_id>", methods = ['GET', 'POST'])
def influencer_adrequests_recieved(influencer_id):
    influencer = Influencer.query.get(influencer_id)
    adrequests_recieved = AdRequest.query.filter_by(influencer_id = influencer_id, owner = "Sponsor").all()

    return render_template("influencer_adrequests_recieved.html", influencer = influencer, adrequests_recieved = adrequests_recieved)

# Influencer View New Ad Requests Recieved [Button]
@app.route("/influencer_view_adrequest_recieved/<int:influencer_id>/<int:adrequest_id>", methods = ['GET', 'POST'])
def influencer_view_adrequest_recieved(influencer_id, adrequest_id):
    influencer = Influencer.query.get(influencer_id)
    adrequest = AdRequest.query.get(adrequest_id)

    return render_template("influencer_view_adrequest_recieved.html", influencer = influencer, adrequest = adrequest)

# Influencer Accept Ad Request Recieved [Button]
@app.route("/influencer_accept_adrequest/<int:influencer_id>/<int:adrequest_id>", methods = ['POST'])
def influencer_accept_adrequest(influencer_id, adrequest_id):
    influencer = Influencer.query.get(influencer_id)
    adrequest = AdRequest.query.get(adrequest_id)

    if adrequest:
        adrequest.status = "Accepted"
        db.session.commit()

        return redirect(f'/influencer_adrequests_recieved/{influencer.id}')
    
# Influencer Reject Ad Request Recieved [Button]
@app.route("/influencer_reject_adrequest/<int:influencer_id>/<int:adrequest_id>", methods = ['POST'])
def influencer_reject_adrequest(influencer_id, adrequest_id):
    influencer = Influencer.query.get(influencer_id)
    adrequest = AdRequest.query.get(adrequest_id)

    if adrequest:
        adrequest.status = "Rejected"
        db.session.commit()

        return redirect(f'/influencer_adrequests_recieved/{influencer.id}')

# Influencer Status of Ad Requests Sent [Page]
@app.route("/influencer_adrequests_sent/<int:influencer_id>", methods = ['GET', 'POST'])
def influencer_adrequests_sent(influencer_id):
    influencer = Influencer.query.get(influencer_id)
    adrequests_sent = AdRequest.query.filter_by(influencer_id = influencer_id, owner = "Influencer").all()

    return render_template("influencer_adrequests_sent.html", influencer = influencer, adrequests_sent = adrequests_sent)

# Influencer View Ad Requests Sent [Button]
@app.route("/influencer_view_adrequest_sent/<int:influencer_id>/<int:adrequest_id>", methods = ['GET', 'POST'])
def influencer_view_adrequest_sent(influencer_id, adrequest_id):
    influencer = Influencer.query.get(influencer_id)
    adrequest = AdRequest.query.get(adrequest_id)

    return render_template("influencer_view_adrequest_sent.html", influencer = influencer, adrequest = adrequest)

# Influencer Update Sent Ad Request [Button]
@app.route("/influencer_update_adrequest/<int:influencer_id>/<int:adrequest_id>", methods = ['GET', 'POST'])
def influencer_update_adrequest(influencer_id, adrequest_id):
    influencer = Influencer.query.get(influencer_id)
    adrequest = AdRequest.query.get(adrequest_id)
    campaign = adrequest.campaign

    if request.method == "POST":
        adrequest.message = request.form.get("adrequest_message")
        adrequest.requirements = request.form.get("adrequest_requirements")
        adrequest.payment_amount = request.form.get("adrequest_payment_amount")

        db.session.commit()

        return redirect(f'/influencer_view_adrequest_sent/{influencer.id}/{adrequest.id}')
    
    return render_template("influencer_update_adrequest.html", influencer = influencer, adrequest = adrequest, campaign = campaign)

# Influencer Delete Ad Request [Button]
@app.route("/influencer_delete_adrequest/<int:influencer_id>/<int:adrequest_id>", methods = ['POST'])
def influencer_delete_adrequest(influencer_id, adrequest_id):
    influencer = Influencer.query.get(influencer_id)
    adrequest = AdRequest.query.get(adrequest_id)

    if adrequest:
        db.session.delete(adrequest)
        db.session.commit()

    return redirect(f'/influencer_adrequests_sent/{influencer.id}')

# SPONSOR ROUTES -----------------------------------------------------------------------------------------

# Sponsor Registration [Page]
@app.route("/sponsor_registration", methods = ['GET', 'POST'])
def sponsor_registration():
    if request.method == "POST":
        sponsor_username = request.form.get("sponsor_username")
        sponsor_password = request.form.get("sponsor_password")
        sponsor_name = request.form.get("sponsor_name")
        sponsor_email = request.form.get("sponsor_email")
        sponsor_industry = request.form.get("sponsor_industry")
        sponsor_budget = request.form.get("sponsor_budget")
        sponsor_description = request.form.get("sponsor_description")
        this_sponsor = Sponsor.query.filter_by(username = sponsor_username).first()

        if this_sponsor:
            return "Username already exists!"
        else:
            new_sponsor = Sponsor(username = sponsor_username, password = sponsor_password, name = sponsor_name, email = sponsor_email, industry = sponsor_industry, budget = sponsor_budget, description = sponsor_description)

            db.session.add(new_sponsor)
            db.session.commit()
            return redirect("/sponsor_login")

    return render_template("sponsor_registration.html")

# Sponsor Login [Page]
@app.route("/sponsor_login", methods = ['GET', 'POST'])
def sponsor_login():
    if request.method == "POST":
        sponsor_username = request.form.get("sponsor_username")
        sponsor_password = request.form.get("sponsor_password")
        this_sponsor = Sponsor.query.filter_by(username = sponsor_username).first()

        if this_sponsor:
            if this_sponsor.password == sponsor_password:
                return redirect(f'/sponsor_dashboard/{this_sponsor.id}')
            else:
                return "Incorrect Password"
        else:
            return "User doesn't exist. Kindly Register first to login."

    return render_template("sponsor_login.html")

# Sponsor Dashboard [Page]
@app.route("/sponsor_dashboard/<int:sponsor_id>", methods = ['GET', 'POST'])
def sponsor_dashboard(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)

    return render_template("sponsor_dashboard.html", sponsor = sponsor)

# Sponsor Profile [Page]
@app.route("/sponsor_profile_page/<int:sponsor_id>", methods = ['GET', 'POST'])
def sponsor_profile_page(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)

    total_spent = 0
    sponsor_campaigns = sponsor.campaigns

    for campaign in sponsor_campaigns:
        payment_sent = AdRequest.query.filter_by(campaign_id = campaign.id, status = "Accepted", influencer_work_status = "Payment Recieved").all()
        total_spent += sum(adrequest.payment_amount for adrequest in payment_sent)

    return render_template("sponsor_profile_page.html", sponsor = sponsor, total_spent = total_spent)

# Sponsor Update Profile [Button]
@app.route("/sponsor_update_profile/<int:sponsor_id>", methods = ['GET', 'POST'])
def sponsor_update_profile(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)

    if request.method == "POST":
        sponsor.username = request.form.get("sponsor_username")
        sponsor.password = request.form.get("sponsor_password")
        sponsor.name = request.form.get("sponsor_name")
        sponsor.email = request.form.get("sponsor_email")
        sponsor.industry = request.form.get("sponsor_industry")
        sponsor.budget = request.form.get("sponsor_budget")
        sponsor.description = request.form.get("sponsor_description")
    
        db.session.commit()

        return redirect(f'/sponsor_profile_page/{sponsor.id}')

    return render_template("sponsor_update_profile.html", sponsor = sponsor)

# Sponsor Delete Account [Button]
@app.route("/delete_sponsor_account/<int:sponsor_id>", methods = ['POST'])
def delete_sponsor_account(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)

    if sponsor:
        for campaign in sponsor.campaigns:
            db.session.query(AdRequest).filter_by(campaign_id = campaign.id).delete()

        db.session.query(Campaign).filter_by(sponsor_id = sponsor_id).delete()
        db.session.delete(sponsor)
        db.session.commit()

    return redirect("/")

# Sponsor My Campaigns [Page]
@app.route("/sponsor_mycampaigns/<int:sponsor_id>", methods = ['GET', 'POST'])
def sponsor_mycampaigns(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)
    my_campaigns = Campaign.query.filter_by(sponsor_id = sponsor_id).all()

    return render_template("sponsor_my_campaigns.html", sponsor = sponsor, my_campaigns = my_campaigns)

# Sponsor Create Campaign [Button]
@app.route("/create_campaign/<int:sponsor_id>", methods = ['GET', 'POST'])
def create_campaign(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)

    if request.method == "POST":
        campaign_name = request.form.get("campaign_name")
        campaign_start_date = request.form.get("campaign_start_date")
        campaign_end_date = request.form.get("campaign_end_date")
        campaign_budget = float(request.form.get("campaign_budget"))
        campaign_visibility = request.form.get("campaign_visibility")
        campaign_target = request.form.get("campaign_target")
        campaign_description = request.form.get("campaign_description")

        new_campaign = Campaign(name = campaign_name, start_date = campaign_start_date, end_date = campaign_end_date, budget = campaign_budget, visibility = campaign_visibility, target = campaign_target, description = campaign_description, sponsor_id = sponsor.id)
        db.session.add(new_campaign)
        db.session.commit()
        return redirect(f'/sponsor_mycampaigns/{sponsor.id}')

    return render_template("sponsor_create_campaign.html", sponsor = sponsor)

# Sponsor View Campaign [Button]
@app.route("/sponsor_view_campaign/<int:sponsor_id>/<int:campaign_id>", methods = ['GET', 'POST'])
def sponsor_view_campaign(sponsor_id, campaign_id):
    sponsor = Sponsor.query.get(sponsor_id)
    campaign = Campaign.query.get(campaign_id)
    all_adrequests = AdRequest.query.filter_by(campaign_id = campaign_id).all()

    return render_template("sponsor_view_campaign.html", sponsor = sponsor, campaign = campaign, all_adrequests = all_adrequests)

# Sponsor Update Campaign [Button]
@app.route("/update_campaign/<int:sponsor_id>/<int:campaign_id>", methods = ['GET', 'POST'])
def update_campaign(sponsor_id, campaign_id):
    sponsor = Sponsor.query.get(sponsor_id)
    campaign = Campaign.query.get(campaign_id)

    if request.method == "POST":
        campaign.name = request.form.get("campaign_name")
        campaign.start_date = request.form.get("campaign_start_date")
        campaign.end_date = request.form.get("campaign_end_date")
        campaign.budget = float(request.form.get("campaign_budget"))
        campaign.visibility = request.form.get("campaign_visibility")
        campaign.target = request.form.get("campaign_target")
        campaign.description = request.form.get("campaign_description")

        db.session.commit()

        return redirect(f'/sponsor_view_campaign/{sponsor.id}/{campaign.id}')

    return render_template("sponsor_update_campaign.html", sponsor = sponsor, campaign = campaign)

# Sponsor Delete Campaign [Button]
@app.route("/delete_campaign/<int:sponsor_id>/<int:campaign_id>", methods = ['POST'])
def delete_campaign(sponsor_id, campaign_id):
    sponsor = Sponsor.query.get(sponsor_id)
    campaign = Campaign.query.get(campaign_id)

    if campaign:
        db.session.query(AdRequest).filter_by(campaign_id = campaign_id).delete()
        db.session.delete(campaign)
        db.session.commit()

    return redirect(f'/sponsor_mycampaigns/{sponsor_id}')

# Sponsor Create Ad Request [Button]
@app.route("/create_adrequest/<int:sponsor_id>/<int:campaign_id>", methods = ['GET', 'POST'])
def create_adrequest(sponsor_id, campaign_id):
    sponsor = Sponsor.query.get(sponsor_id)
    campaign = Campaign.query.get(campaign_id)
    influencer_list = Influencer.query.filter_by(flag_status = "Unflagged").all()

    if request.method == "POST":
        adrequest_message = request.form.get("adrequest_message")
        adrequest_requirements = request.form.get("adrequest_requirements")
        adrequest_payment_amount = request.form.get("adrequest_payment_amount")
        adrequest_owner = "Sponsor"
        adrequest_influencer_id = request.form.get("adrequest_influencer")

        new_adrequest = AdRequest(message = adrequest_message, requirements = adrequest_requirements, payment_amount = adrequest_payment_amount, owner = adrequest_owner, campaign_id = campaign.id, influencer_id = adrequest_influencer_id)

        db.session.add(new_adrequest)
        db.session.commit()

        return redirect(f'/sponsor_adrequests_sent/{sponsor.id}')

    return render_template("sponsor_create_adrequest.html", sponsor = sponsor, campaign = campaign, influencer_list = influencer_list)

# Sponsor Monitor Influencers' Work [Page]
@app.route("/sponsor_monitor_influencers/<int:sponsor_id>", methods = ['GET', 'POST'])
def sponsor_monitor_influencers(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)
    accepted_adrequests = AdRequest.query.join(Campaign).filter(Campaign.sponsor_id == sponsor_id, AdRequest.status == "Accepted").all()

    return render_template("sponsor_monitor_influencers.html", sponsor = sponsor, accepted_adrequests = accepted_adrequests)

# Sponsor Payment Actions [Button]
@app.route("/sponsor_payment_actions/<int:sponsor_id>/<int:adrequest_id>", methods = ['POST'])
def sponsor_payment_actions(sponsor_id, adrequest_id):
    sponsor = Sponsor.query.get(sponsor_id)
    adrequest = AdRequest.query.get(adrequest_id)

    if adrequest:
        if adrequest.influencer_work_status == "Confirmation Pending":
            adrequest.influencer_work_status = "Payment Pending"
        elif adrequest.influencer_work_status == "Payment Pending":
            adrequest.influencer_work_status = "Payment Recieved"

        db.session.commit()

    return redirect(f'/sponsor_monitor_influencers/{sponsor.id}')

# Sponsor View Work [Button]
@app.route("/sponsor_view_work/<int:sponsor_id>/<int:adrequest_id>", methods = ['GET', 'POST'])
def sponsor_view_work(sponsor_id,adrequest_id):
    sponsor = Sponsor.query.get(sponsor_id)
    adrequest = AdRequest.query.get(adrequest_id)

    return render_template("sponsor_view_work.html", sponsor = sponsor, adrequest = adrequest)

# Sponsor Find an Influencer [Page]
@app.route("/find_influencers/<int:sponsor_id>", methods = ['GET', 'POST'])
def sponsor_find_influencers(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)
    find_influencers = Influencer.query.all()

    return render_template("sponsor_find_influencers.html", sponsor = sponsor, find_influencers = find_influencers)

# Sponsor Search Influencers [Page]
@app.route("/sponsor_search_influencers/<int:sponsor_id>", methods = ['GET', 'POST'])
def sponsor_search_influencers(sponsor_id):

    sponsor = Sponsor.query.get(sponsor_id)

    if request.method == "POST":
        search_word = request.form.get("search_word")
        return redirect(f'/sponsor_search_influencers/{sponsor.id}?search_word={search_word}')

    search_word = request.args.get('search_word', '')
    
    if search_word:
        search = f"%{search_word}%"
        name_results = Influencer.query.filter(Influencer.name.like(search)).all()
        category_results = Influencer.query.filter(Influencer.category.like(search)).all()
        reach_results = Influencer.query.filter(Influencer.reach.like(search)).all()
        result_influencers = name_results + category_results + reach_results
    else:
        result_influencers = []

    return render_template("sponsor_search_influencers.html", sponsor = sponsor, result_influencers = result_influencers, search_word = search_word)

# Sponsor View Influencer [Button]
@app.route("/sponsor_view_influencer/<int:sponsor_id>/<int:influencer_id>", methods = ['GET', 'POST'])
def sponsor_view_influencer(sponsor_id, influencer_id):
    sponsor = Sponsor.query.get(sponsor_id)
    influencer = Influencer.query.get(influencer_id)
    accepted_adrequests = AdRequest.query.filter_by(influencer_id = influencer_id, status = "Accepted").all()

    return render_template("sponsor_view_influencer.html", sponsor = sponsor, influencer = influencer, accepted_adrequests = accepted_adrequests)

# Sponsor Send a Request to an Influencer [Button]
@app.route("/sent_adrequest_to_influencer/<int:sponsor_id>/<int:influencer_id>", methods = ['GET', 'POST'])
def sent_adrequest_to_influencer(sponsor_id, influencer_id):
    sponsor = Sponsor.query.get(sponsor_id)
    influencer = Influencer.query.get(influencer_id)
    campaign_list = Campaign.query.filter_by(sponsor_id = sponsor_id, flag_status = "Unflagged").all()

    if request.method == "POST":
        adrequest_message = request.form.get("adrequest_message")
        adrequest_requirements = request.form.get("adrequest_requirements")
        adrequest_payment_amount = request.form.get("adrequest_payment_amount")
        adrequest_owner = "Sponsor"
        adrequest_campaign = request.form.get("adrequest_campaign")

        new_adrequest = AdRequest(message = adrequest_message, requirements = adrequest_requirements, payment_amount = adrequest_payment_amount, owner = adrequest_owner, campaign_id = adrequest_campaign, influencer_id = influencer.id)
        db.session.add(new_adrequest)
        db.session.commit()
        return redirect(f'/sponsor_adrequests_sent/{sponsor.id}')

    return render_template("sponsor_send_adrequest_to_influencer.html", sponsor = sponsor, influencer = influencer, campaign_list = campaign_list)

# Sponsor New Ad Requests Recieved [Page]
@app.route("/sponsor_adrequests_recieved/<int:sponsor_id>", methods = ['GET', 'POST'])
def sponsor_adrequests_recieved(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)
    adrequests_recieved = AdRequest.query.join(Campaign).filter(Campaign.sponsor_id == sponsor_id, AdRequest.owner == "Influencer").all()

    return render_template("sponsor_adrequests_recieved.html", sponsor = sponsor, adrequests_recieved = adrequests_recieved)

# Sponsor View Ad Requests Recieved [Button]
@app.route("/sponsor_view_adrequest_recieved/<int:sponsor_id>/<int:adrequest_id>", methods = ['GET', 'POST'])
def sponsor_view_adrequest_recieved(sponsor_id, adrequest_id):
    sponsor = Sponsor.query.get(sponsor_id)
    adrequest = AdRequest.query.get(adrequest_id)

    return render_template("sponsor_view_adrequest_recieved.html", sponsor = sponsor, adrequest = adrequest)

# Sponsor Accept Ad Request Recieved [Button]
@app.route("/sponsor_accept_adrequest/<int:sponsor_id>/<int:adrequest_id>", methods = ['POST'])
def sponsor_accept_adrequest(sponsor_id, adrequest_id):
    sponsor = Sponsor.query.get(sponsor_id)
    adrequest = AdRequest.query.get(adrequest_id)

    if adrequest:
        adrequest.status = "Accepted"
        db.session.commit()

        return redirect(f'/sponsor_adrequests_recieved/{sponsor.id}')
    
# Sponsor Reject Ad Request Recieved [Button]
@app.route("/sponsor_reject_adrequest/<int:sponsor_id>/<int:adrequest_id>", methods = ['POST'])
def sponsor_reject_adrequest(sponsor_id, adrequest_id):
    sponsor = Sponsor.query.get(sponsor_id)
    adrequest = AdRequest.query.get(adrequest_id)

    if adrequest:
        adrequest.status = "Rejected"
        db.session.commit()

        return redirect(f'/sponsor_adrequests_recieved/{sponsor.id}')

# Sponsor Status of Ad Requests Sent [Page]
@app.route("/sponsor_adrequests_sent/<int:sponsor_id>", methods = ['GET', 'POST'])
def sponsor_adrequests_sent(sponsor_id):
    sponsor = Sponsor.query.get(sponsor_id)
    adrequests_sent = AdRequest.query.join(Campaign).filter(Campaign.sponsor_id == sponsor_id, AdRequest.owner == "Sponsor").all()

    return render_template("sponsor_adrequests_sent.html", sponsor = sponsor, adrequests_sent = adrequests_sent)

# Sponsor View Ad Requests Sent [Button]
@app.route("/sponsor_view_adrequest_sent/<int:sponsor_id>/<int:adrequest_id>", methods = ['GET', 'POST'])
def sponsor_view_adrequest_sent(sponsor_id, adrequest_id):
    sponsor = Sponsor.query.get(sponsor_id)
    adrequest = AdRequest.query.get(adrequest_id)

    return render_template("sponsor_view_adrequest_sent.html", sponsor = sponsor, adrequest = adrequest)

# Sponsor Update Sent Ad Request [Button]
@app.route("/sponsor_update_adrequest/<int:sponsor_id>/<int:adrequest_id>", methods = ['GET', 'POST'])
def sponsor_update_adrequest(sponsor_id, adrequest_id):
    sponsor = Sponsor.query.get(sponsor_id)
    adrequest = AdRequest.query.get(adrequest_id)
    campaign = adrequest.campaign
    influencer_list = Influencer.query.filter_by(flag_status = "Unflagged").all()
    campaign_list = Campaign.query.filter_by(sponsor_id = sponsor_id, flag_status = "Unflagged").all()

    selected_campaign_id = adrequest.campaign_id
    selected_influencer_id = adrequest.influencer_id

    if request.method == "POST":
        adrequest.message = request.form.get("adrequest_message")
        adrequest.requirements = request.form.get("adrequest_requirements")
        adrequest.payment_amount = request.form.get("adrequest_payment_amount")
        adrequest.influencer_id = request.form.get("adrequest_influencer")
        adrequest.campaign_id = request.form.get("adrequest_campaign")

        db.session.commit()

        return redirect(f'/sponsor_view_adrequest_sent/{sponsor.id}/{adrequest.id}')
    
    return render_template("sponsor_update_adrequest.html", sponsor = sponsor, adrequest = adrequest, campaign = campaign, selected_campaign_id = selected_campaign_id, selected_influencer_id = selected_influencer_id, influencer_list = influencer_list, campaign_list = campaign_list)

# Sponsor Delete Ad Request [Button]
@app.route("/sponsor_delete_adrequest/<int:sponsor_id>/<int:adrequest_id>", methods = ['POST'])
def sponsor_delete_adrequest(sponsor_id, adrequest_id):
    sponsor = Sponsor.query.get(sponsor_id)
    adrequest = AdRequest.query.get(adrequest_id)

    if adrequest:
        db.session.delete(adrequest)
        db.session.commit()

    return redirect(f'/sponsor_adrequests_sent/{sponsor.id}')