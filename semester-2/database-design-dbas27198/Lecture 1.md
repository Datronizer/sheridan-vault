# Data
Data is simply information! The information could be anything. It could be as simple as binary or as complicated as a 10hr FNAF lore video.
## Definition
**Database**: Organized Collection of logically related data (DBs store data, duh)
**Data**: Stored representations of meaningful objects and events
- Structured : numbers, text, dates
- Unstructured: images, video, documents
**Information**:  data processed to increase knowledge in the person using the database
**Metadata**: data that describes the properties and context of user data (basically data about data)
## Data in Context
Let's say I hand you a cluster of data with no ordering or tags or headers. How would you know what's what? The answer is: you wouldn't. There's almost no way to dissect this data unless you have a ton of free time. 

Or, unless the data has context provided. 

Context allows us to understand our stored data as they provide additional identifying information, this could be headers or tags or datatypes.

Metadata is one of these. They provide descriptions of the properties or characteristics of the data, including data types, field sizes, allowable values, and data context.
# The DATABASE approach
The Database Approach aims to have a central repository of shared data, data that will be managed by a controlling agent, and is stored in a standardized, convenient form. 

Of course this requires a Database Management System (DBMS). This system, drum roll please, is MySQL... or Oracle, Microsoft Access, PostgreSQL, MongoDB, etc. Jesus there's so many of these.
## Database Management System
A DBMS is a software system that is used to create, maintain, and provide controlled access to the user databases. You could say it manages data resources the same way an operating system manages hardware resources.
### Advantages
- Program-data independence
- Planned data redundancy
- Data consistency, sharing
- Increased productivity
- Enforcement of standards
- Improved data quality, accessibility, and responsiveness
- Reduced maintenance
- Improved decision support
### Disadvantages
- New, specialized personnel
- Installation and management cost and complexity
- Conversion costs
- Need for explicit backup and recovery
- Organizational conflict
# Relationship
## One to One
When one object A contains **exactly one** object B, and object B contains **exactly one** object A, the relation is called a One-to-One relation. 

This relation rarely happens. The only instance I have seen this is membership relations: 1 membership key for 1 user, assuming this database only covers 1 venue.
## One to Many


## Many to One

## Many to Many

# Database Environment
- CASE tools: Computer-aided software engineering.
- Repository: Centralized storehouse of metadata
- Database Management System (DBMS): Software for managing the database
- Database: Storehouse of the data
- Application Programs: Software using the data
- User Interface: Text and Graphical displays to users
- Data/Database Administration: Personnel responsible for maintaining the data/database.
- System Developers: Personnel responsible for designing databases and software
- End user: people who use the applications and databases
# Evolution of Database Technologies
The DB system we're seeing today was not grown overnight. Lots of features were added and removed as time goes on, here is a timeline of the features that were added over time.
%% Insert Image here %%

# Database Architectures
There are multiple different database models and the use of which is dependent on your project. In any case, you can display this data in different ways: Multidimensional Cube View and Multi-schema-view.

# Entreprise Database Applications
## Enterprise Resource Planning (ERP)
Integrates all enterprise functions:
- Manufacturing, finance, sales, marketing, inventory, accounting, human resources.
## Data Warehouse
Integrated decision support system derived from various operational databases.
