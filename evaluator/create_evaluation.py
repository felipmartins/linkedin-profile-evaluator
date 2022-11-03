from .models import Evaluation
from .linkedin_evaluator import scrape_linkedin


def new_evaluation(user):

    user_dic = scrape_linkedin(user)

    new_eval = Evaluation(
        url_name=user_dic["url_name"],
        full_name=user_dic["full_name"],
        profile_image=user_dic["profile_image"],
        has_changed_profile_image=user_dic["has_changed_profile_image"],
        face_found_in_profile_image=user_dic["face_found_in_profile_image"],
        background_image=user_dic["background_image"],
        has_changed_background_image=user_dic["has_changed_background_image"],
        connections=user_dic["connections"],
        about=user_dic["about"],
        head_title=user_dic["head_title"],
        contact_info=user_dic["contact_info"],
        education=user_dic["education"],
        skills=user_dic["skills"],
        num_skills=len(user_dic["skills"]),
        recommendations=user_dic["recommendations"],
        num_recommendations=len(user_dic["recommendations"]),
        experience=user_dic["experience"],
        projects=user_dic["projects"],
        num_projects=len(user_dic["projects"]),
        certifications=user_dic["certifications"],
        languages=user_dic["languages"],
        authoral_posts=user_dic["authoral_posts"],
    )

    return new_eval