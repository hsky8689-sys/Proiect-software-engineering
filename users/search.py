from django.http import JsonResponse
from django.db.models import Q

from projects.models import Project
from users.models import User, UserProfileData


class SearchFilterData():
    def __init__(self,user_id:int,query:str,search_type,sort_by_date,sort_by_relevance):
        self.user_id = user_id
        self.query = query
        self.search_type = search_type
        self.sort_by_date = sort_by_date
        self.sort_by_relevance = sort_by_relevance
        self.page_index = 0
        self.pages_number = 0
class SearchManager():
    def __init__(self):
        self.results = {'people':[],'projects':[]}
    def execute_search(self,filter_data):
        self.results = {'people':[],'projects':[]}
        from devnetwork import settings
        if not filter_data.search_type in settings.SEARCH_TYPE:
            return JsonResponse({
                'status': 'unknown search type',
                'results': {'results':[]}
            })
        if filter_data.search_type == 'PEOPLE':
            people = User.objects.filter(
                username__icontains=filter_data.query,
                email__icontains=filter_data.query
            ).values('id', 'username', 'email')[:20]
            self.results['people']= people
        elif filter_data.search_type == 'PROJECTS':
            pass
        elif filter_data.search_type == 'ALL':
            self.results['people'] = list(User.objects.filter(
                username__icontains=filter_data.query,
                email__icontains=filter_data.query,
            ).values('id', 'username')[:20])

            profile_data = UserProfileData.objects
            for user in self.results['people']:
                user['profile_picture'] = (profile_data.get_profile_data(User(id=user['id']))
                                                      .profile_picture.name)

            self.results['projects'] = list(Project.objects.filter(
                Q(name__icontains=filter_data.query)|
                Q(description__icontains=filter_data.query)
            ).values('id','name','description')[:20])
    def get_results_from_search(self):
            return self.results
