from pydantic import AnyUrl, ValidationError, BaseModel
from typing import List, Dict, Optional, Any
from enum import Enum

class DataciteIdentifier(BaseModel):
    
    class DataciteIdentifierType(Enum):
        DOI="DOI"
    
    identifier: str = ""
    identifierType: DataciteIdentifierType


class DataciteCreator(BaseModel):
    creatorName: str
    nameIdentifiers: Optional[str]
    affiliations : Optional[List[str]]
    familyName: Optional[str]
    givenName: Optional[str]


class DataciteTitle(BaseModel):
    
    class DataciteTitleType(Enum):
        AlternativeTitle = "AlternativeTitle"
        Subtitle = "Subtitle"
        TranslatedTitle = "TranslatedTitle"
        Other = "Other"
    
    title: str = ""
    type: Optional[DataciteTitleType]
    lang: Optional[str]        


class DataciteSubject(BaseModel):
    subject : str = ""
    subjectScheme : Optional[str] = ""
    schemeURI: Optional[AnyUrl] = ""
    valueURI: Optional[AnyUrl] = ""
    lang : str = ""


class DataciteResourceType(BaseModel):

    class DataciteResourceTypeGeneral(Enum):
        Audiovisual = "Audiovisual"
        Collection = "Collection"
        Dataset = "Dataset"
        Event = "Event"
        Image = "Image"
        InteractiveResource = "InteractiveResource"
        Model = "Model"
        PhysicalObject = "PhysicalObject"
        Service = "Service"
        Software = "Software"
        Sound = "Sound"
        Text = "Text"
        Workflow = "Workflow"
        Other = "Other"

    resourceType : Optional[str] = ""
    resourceTypeGeneral: DataciteResourceTypeGeneral = None


class DataciteContributor(BaseModel):
    
    class DataciteContributorType(Enum):
        ContactPerson = "ContactPerson"
        DataCollector = "DataCollector"
        DataCurator = "DataCurator"
        DataManager = "DataManager"
        Editor = "Editor"
        HostingInstitution = "HostingInstitution"
        Other = "Other"
        Producer = "Producer"
        ProjectLeader = "ProjectLeader"
        ProjectManager = "ProjectManager"
        ProjectMember = "ProjectMember"
        RegistrationAgency = "RegistrationAgency"
        RegistrationAuthority = "RegistrationAuthority"
        RelatedPerson = "RelatedPerson"
        ResearchGroup = "ResearchGroup"
        RightsHolder = "RightsHolder"
        Researcher = "Researcher"
        Sponsor = "Sponsor"
        Supervisor = "Supervisor"
        WorkPackageLeader = "WorkPackageLeader"
        
    contributorType: DataciteContributorType = None
    contributorName: str = ""
    affiliations: Optional[List[str]] = []
    familyName: Optional[str] = ""
    givenName: Optional[str] = ""
    
class DataciteAlternateIdentifier(BaseModel):
    alternateIdentifier: str = ""
    alternateIdentifierType : str = ""

class DataciteRelatedIdentifier(BaseModel):
    
    class DataciteRelatedIdentifierType(Enum):
        ARK = "ARK"
        arXiv = "arXiv"
        bibcode = "bibcode"
        DOI = "DOI"
        EAN13 = "EAN13"
        EISSN = "EISSN"
        Handle = "Handle"
        IGSN = "IGSN"
        ISBN = "ISBN"
        ISSN = "ISSN"
        ISTC = "ISTC"
        LISSN = "LISSN"
        LSID = "LSID"
        PMID = "PMID"
        PURL = "PURL"
        UPC = "UPC"
        URL = "URL"
        URN = "URN"
        
    class DataciteRelationType(Enum):
        IsCitedBy = "IsCitedBy"
        Cites = "Cites"
        IsSupplementTo = "IsSupplementTo"
        IsSupplementedBy = "IsSupplementedBy"
        IsContinuedBy = "IsContinuedBy"
        Continues = "Continues"
        IsNewVersionOf = "IsNewVersionOf"
        IsPreviousVersionOf = "IsPreviousVersionOf"
        IsPartOf = "IsPartOf"
        HasPart = "HasPart"
        IsReferencedBy = "IsReferencedBy"
        References = "References"
        IsDocumentedBy = "IsDocumentedBy"
        Documents = "Documents"
        IsCompiledBy = "IsCompiledBy"
        Compiles = "Compiles"
        IsVariantFormOf = "IsVariantFormOf"
        IsOriginalFormOf = "IsOriginalFormOf"
        IsIdenticalTo = "IsIdenticalTo"
        HasMetadata = "HasMetadata"
        IsMetadataFor = "IsMetadataFor"
        Reviews = "Reviews"
        IsReviewedBy = "IsReviewedBy"
        IsDerivedFrom = "IsDerivedFrom"
        IsSourceOf = "IsSourceOf"
        
    relatedIdentifer : str = ""
    relatedIdentiferType : DataciteRelatedIdentifierType = None
    relatedMetadataScheme: str = ""
    schemeURI : AnyUrl = "" 

class DataciteRightsList(BaseModel):
    rightsURI: AnyUrl = ""
    rights: str = ""
        
class DataciteDescription(BaseModel):
    
    class DataciteDescriptionType(Enum):
        Abstract = "Abstract"
        Methods = "Methods"
        SeriesInformation = "SeriesInformation"
        TableOfContents = "TableOfContents"
        TechnicalInfo = "TechnicalInfo"
        Other = "Other"
        
    description: str = ""
    descriptionType : DataciteDescriptionType = None
    lang : Optional[str] = ""

class DataciteFundingReferences(BaseModel):
    
    class DataciteFunderIdentifier(Enum):
        ISNI = "ISNI"
        GRID = "GRID"
        CrossrefFunderID = "Crossref Funder ID"
        Other = "Other"
        
    class DataciteAward(BaseModel):
        awardNumber : str = ""
        awardURI: AnyUrl = ""
        
    funderName: str = ""
    funderIdentifier: Optional[DataciteFunderIdentifier] = None
    awardNumber: Optional[DataciteAward] = None
    awardTitle: Optional[str] = ""
        
class DataciteGeoLocation(BaseModel):
    
    class DataciteGeoLocationPoint(BaseModel):
        pointLongitude: float
        pointLatitude: float
            
    class DataciteGeoLocationBox(BaseModel):
        westBoundLongitude: float
        eastBoundLongitude: float
        southBoundLatitude: float
        northBoundLatitude: float
    
    geoLocationPoint: Optional[DataciteGeoLocationPoint]
    geoLocationBox: Optional[DataciteGeoLocationBox]
    geoLocationPlace : Optional[str]
    geoLocationPolygon: Optional[List[DataciteGeoLocationPoint]] # Add min items 3
        
class Datacite(BaseModel):
    # Required fields
    identifier: DataciteIdentifier
    creators: List[DataciteCreator]
    titles: List[DataciteTitle]
    publisher : str 
    publicationYear : str
    resourceType: DataciteResourceType 
        
    # Optional fields
    subjects : Optional[List[DataciteSubject]]
    resourceType : Optional[DataciteResourceType]
    contributors : Optional[List[DataciteContributor]]
    language: Optional[str]
    alternateIdentifiers : Optional[List[DataciteAlternateIdentifier]]
    relatedIdentifiers: Optional[List[DataciteRelatedIdentifier]]
    sizes : Optional[List[str]]
    formats : Optional[List[str]]
    version : Optional[List[str]]
    rightsList: Optional[DataciteRightsList]
    descriptions: Optional[DataciteDescription]
    fundingReferences: Optional[DataciteFundingReferences]
    geoLocations: Optional[DataciteGeoLocation]

    __datacite_version : Optional[str] = "4.3"

    def to_json(self, exclude_unset=True, indent=2):
        return self.json(exclude_unset=exclude_unset, indent=indent)

    def to_xml(self):
        pass
    
    def describe(self):
        print("Titles: {}".format([title.title for title in self.titles]))
        print("Creators: {}".format([creator.creatorName for creator in self.creators]))
        print("Publisher: {}".format(self.publisher))
        print("Publication year: {}".format(self.publicationYear))
        print()
        print("== Datacite version: {}".format(self.__datacite_version))
        
    # Helper functions
    def add_title(self, **kwargs):
        self.titles.append(DataciteTitle(**kwargs))
        
    def add_creator(self, **kwargs):
        self.creators.append(DataciteCreator(**kwargs))
        
    def add_contributor(self, **kwargs):
        if self.contributors:
            self.contributors.append(DataciteContributor(**kwargs))
        else: self.contributors = [DataciteContributor(**kwargs)]