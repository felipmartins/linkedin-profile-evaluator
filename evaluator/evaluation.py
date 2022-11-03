from .create_evaluation import new_evaluation

def validate_conditions(user):

    evaluation = new_evaluation(user)

    contact_values =  evaluation.contact_info.values()
    for elem in contact_values:
        if '@' in elem:
            evaluation.has_email_in_contact_info = True
            break
    
    for elem in contact_values:
        if 'github' in elem:
            evaluation.has_github_in_contact_info = True
            break
    
    if 'desenvolvedor' in evaluation.head_title or 'developer' in evaluation.head_title or 'front' in evaluation.head_title or 'back' in evaluation.head_title or 'full' in evaluation.head_title:
        evaluation.has_key_words_in_title = True
    
    if evaluation.about:
        evaluation.has_about_section = True
    
    for elem in evaluation.education.values():
        if 'trybe' in elem.lower():
            evaluation.has_trybe_in_education = True
            break
    
    if evaluation.authoral_posts >= 3:
        evaluation.has_3_or_more_authoral_posts = True
    
    if len(evaluation.skills) >= 3:
        evaluation.has_3_or_more_skills = True
    
    if len(evaluation.projects) >= 3:
        evaluation.has_3_or_more_projects = True
    
    if len(evaluation.recommendations) >= 3:
        evaluation.has_3_or_more_recommendations = True
    
    if evaluation.connections >= 200:
        evaluation.has_200_or_more_connections = True

    return evaluation


def check_grade(user):

    evaluation = validate_conditions(user)

    grade = 0

    if evaluation.has_changed_profile_image:
        grade += 5

        if evaluation.face_found_in_profile_image:
            grade += 5
    
    if evaluation.has_changed_background_image:
        grade += 5
    
    if evaluation.has_email_in_contact_info:
        grade += 5
    
    if evaluation.has_github_in_contact_info:
        grade += 5
    
    if evaluation.has_key_words_in_title:
        grade += 10
    
    if evaluation.has_about_section:
        grade += 10
    
    if evaluation.has_trybe_in_education:
        grade += 5
    
    if evaluation.has_3_or_more_authoral_posts:
        grade += 10
    
    if evaluation.has_3_or_more_skills:
        grade += 10
    
    if evaluation.has_3_or_more_projects:
        grade += 10
    
    if evaluation.has_3_or_more_recommendations:
        grade += 10
    
    if evaluation.has_200_or_more_connections:
        grade += 10
    
    evaluation.grade = grade

    evaluation.save()

    return evaluation