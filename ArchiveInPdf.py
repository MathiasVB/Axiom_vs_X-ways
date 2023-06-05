from axiom import *

class HiddenZipArtifact(Artifact):
  def __init__(self):
    self.AddHunter(HiddenZip())

  def GetName(self):
    return 'Find possible hidden archives in pdf'

  def CreateFragments(self):
    self.AddFragment("FileName", Category.None, FragmentType.String)

class HiddenZip(CarvingHunter):
  def __init__(self):
    self.AddSimpleMagic(bytes([0x37, 0x7A, 0xBC, 0xAF, 0x27])) # 7z
    self.AddSimpleMagic(bytes([0x50, 0x4b, 0x03, 0x04])) # zip
    self.Platform = Platform.Computer 

  def Register(self, registrar):
    self.Log("Registering Hidden Archive hunter")
    registrar.RegisterFileExtension(".pdf")
    registrar.RegisterCarver()


  def Hunt(self, context):
    self.Log("Inside Hunt function")
    self.Log(str(context.Searchable.Path))
    
    if str(context.Searchable.Path).endswith(".pdf"):
        hit = Hit()
        hit.SetLocation(context.FoundMagic.FoundSpot)
        hit.AddValue('FileName', context.Searchable.Path)

        self.PublishHit(hit)
    else:
        pass
        
        

RegisterArtifact(HiddenZipArtifact())


