## List, Objects, etc are containers
## we can create Custom contianer

## Container is holds data with instance and provides some methods to control

## Container for collect Tags with custom methods
class TagCloud:
    def __init__(self, aTags = []):
        self.tags = {} # Dictionary to store tags and count
        for sTag in aTags:
            self.addTag(sTag)
    
    def addTag(self, tag):
        # Add tag & no.of times count
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    ## Magic methods to access & handle contianer in standard way 

    def __setitem__(self, sTag, iCount): # enables to set/overwrite tag directly with '=' from out side 
        self.tags[sTag.lower()] = iCount
    
    def __len__(self): # enables to get total tags using 'len' fucntion
        return len(self.tags)
    
    def __iter__(self): # enable to iterate tags in loops
        return iter(self.tags)


### Test Container
myTags = TagCloud(["MB", "BM"])
myTags.addTag("BM")
myTags.addTag("BM")
myTags.addTag("Python")

print(myTags.tags)

## Set Item
myTags["Hello"] = 10
myTags["BM"] = 20

print(myTags.tags)

## Tags lenth
print(len(myTags))

##