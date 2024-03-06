from .models import Setting

def SettingList(request):
  try:
     context=Setting.objects.get()
  except:
     context=None
  return {'setting':context}