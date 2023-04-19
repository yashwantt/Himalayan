

def uploadImages(path_of_the_directory):
    from .models import Image
    import os
    from django.core.files import File 
    for filename in os.listdir(path_of_the_directory):
            print(filename)
            title = str(filename)
            img = os.path.join(path_of_the_directory, filename)
            j = Image.objects.create(title = title, img = File(open(img,'rb')))
            j.save()
                


def readDocx(file_path, city):
    import docx
    from .models import Package, Pack_Desc, Popular_Destination
    doc = docx.Document(file_path)
    paras = doc.paragraphs

    i = 0
    while i < len(paras):
        if paras[i].runs == [] or paras[i].runs[0].font.size != 254000:
            i+=1
            continue
        head = paras[i].text
        volvo = False
        if "volvo" in head.lower():
            volvo = True
        if "EX " in head:
            head = head[:head.find("EX ")]
        i+=1
        k = paras[i].text.replace("DURATION:", "")
        k = k.replace("DAYS", "")
        k = k.split("NIGHTS")
        days = int(k[0])
        nights = int(k[1])

        i+=1

        start = paras[i].text.replace("STARING POINT: ", "")

        i+=2

        overview = ""
        while "SHORT ITINERARY" not in paras[i].text:
            overview = overview + "<br>" + paras[i].text 
            i+=1
        i+=1
        while paras[i].runs == []:
            i+=1
        pack_desc = []
        while True:
            if paras[i].runs == []:
                i+=1
                continue
            if "INCLUSIONS" in paras[i].text:
                break
            day = int(paras[i].text.replace("DAY ", ""))
            i+=1
            while paras[i].runs == []:
                i+=1
            title = paras[i].text
            i+=1
            desc = ""
            while True:
                if paras[i].runs == []:
                    i+=1
                    continue
                elif "DAY " in paras[i].text or "INCLUSIONS" in paras[i].text:
                    break
                else:
                    desc = desc + f"<li>{paras[i].text}</li>"
                    i+=1
            pack_desc.append((day,title,desc))
        pack = Package.objects.create(title = head,days = days, nights = nights, starting_from = start, desc = overview,  volvo = volvo )
        returnedQS = Popular_Destination.objects.filter(title = city)
        for m in returnedQS.iterator():
            pack.cities.add(m)
        pack.save()
        for j in pack_desc:
            pd = Pack_Desc.objects.create(day = j[0], title =j[1], desc = j[2], package = pack)
            pd.save()
        print(head)

# front_img = Image.objects.filter(title = f"{city} Front.jpg").first().img.path, main_img = Image.objects.filter(title = f"{city} Main.jpg").first().img.path,

def loadDesc():
    from .models import Image, Pack_Desc
    l = [
     "Local Manali",
     "To Udaipur",
     "To Keylong",
     "To Sarchu",
     "To Manali",
     "To Kullu",
     "to delhi chandigarh",
     "delhi to",
     "SOLANG - VASHISHT",
     "TO BARALACHA LA",
     "explore manali",
     "to chandertaal",
     "to tabo",
     "kibber sanctury",
     "langza",
     "rohtang pass",
     "hatu kufri", "kufri naldhera",
     "local shimla",
     "via chitkul",
     "to sangla",
     "explore spiti", 
     "to kalpa", 
     "to sarahan",
     "local amritsar",
     "to amritsar", 
     "mini switzerland",
     "to dalhousie",
     "local dalhousie",
     "local dharamshala",
     "to dharamshala",
     "to pin valley",
     "chamba",
     "to palampur", 
     "to pathankot",
     "bir adventure",
     "to bir",
     "to shimla",
     "to kaza",
     "delhi (",
    ]
    ab = 0
    qs = Pack_Desc.objects.all()
    for j in l:
        print(j, end = " ")
        url = Image.objects.get(title__contains = j).img.url
        k = 0
        for i in qs:
            if j.lower() in i.title.lower():
                i.img = url
                i.save()
                k += 1
                ab+=1
        print(k)
        
    print(ab)
    


   
# l = [
#     "Local Manali",
#      "To Udaipur",
#      "To Keylong",
#      "To Sarchu",
#      "To Manali",
#      "To Kullu",
#      "to delhi chandigarh",
#      "delhi to",
#      "SOLANG - VASHISHT",
#      "TO BARALACHA LA",
#      "explore manali",
#      "to chandertaal",
#      "to tabo",
#      "kibber sanctury",
#      "langza",
#      "rohtang pass",
#      "hatu kufri", "kufri naldhera"
#      "local shimla",
#      "via chitkul",
#      "to sangla",
#      "explore spiti", 
#      "to kalpa", 
#      "to sarahan",
#      "local amritsar",
#      "to amritsar", 
#      "mini switzerland",
#      "to dalhousie",
#      "local dalhousie",
#      "local dharamshala",
#      "to dharamshala",
#      "to pin valley",
#      "chamba",
#      "to palampur", 
#      "to pathankot",
#      "bir adventure",
#      "to bir"
# ]

 
