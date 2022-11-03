from django.shortcuts import render, redirect, get_object_or_404
from .evaluation import check_grade
from .models import Evaluation

def index(request):
    context = {}
    if request.method == "POST":
        user = request.POST["linkedin_user"]
        new_eval = check_grade(user)
        return redirect("evaluation", uuid=new_eval.uuid)
    return render(request, "index.html", context)


def evaluation(request, uuid: str):
    current_evaluation = get_object_or_404(Evaluation, uuid=uuid)
    context = {"evaluation": current_evaluation}
    return render(request, "evaluation.html", context)