import enum

class Genre(enum.Enum):
  Alternative = 'Alternative'
  Blue = 'Blue'
  Classical = 'Classical'
  Country = 'Country' 
  Electronic = 'Electronic'  
  Folk = 'Folk' 
  Funk = 'Funk' 
  Hip-Hop = 'Hip-Hop' 
  Heavy Metal = 'Heavy Metal' 
  Instrumental = 'Instrumental' 
  Jazz = 'Jazz' 
  Musical Theatre = 'Musical Theatre' 
  Pop = 'Pop' 
  Punk = 'Punk' 
  R&B = 'R&B' 
  Reggae = 'Reggae' 
  Rock n Roll = 'Rock n Roll' 
  Soul = 'Soul' 
  Other = 'Other' 

  @classmethod
  def choices(cls):
    """Methods decorated with @classmethod can be called statically without having an instance of the class."""
    return [(choice.name, choice.value) for choice in cls]
