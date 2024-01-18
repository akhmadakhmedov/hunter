from django.shortcuts import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse('Helloooou')


def about(request):
    return HttpResponse("About us info's")


def contact(request):
    return HttpResponse("Here are all the contacts")

def address(request):
    return HttpResponse("""
                <div>
                    <li>Pakhta abad str 144 Osh, Kyrgyzstan</li>
                    <li>Pereulok geologcheskaya 345, Bishkek</li>
                </div>
                """)
