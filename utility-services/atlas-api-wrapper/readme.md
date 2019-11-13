# Atlas API wrapper

This is the API wrapper for [Apache Atlas](https://atlas.apache.org/#/). API Wrapper is a scalable and extensible set of core Atlas foundational governance services APIs . One way to use API wrapper is through a REST API, with operations that create and manage Entities, Relationships, implement search features, execute queries, and handle results in Atlas.

## Key concepts

API Wrapper has the concepts of Entities, TypeDefs, Relationships and Searches. Data is typically pushed to Atlas via JSON from an external data source.

There are several types of operations that can be executed against the service:

* [Entities operations](http://atlas.apache.org/api/v2/resource_EntityREST.html). As on today, below operations are supported for entities
	*   Entity bulk API: - Get,  Delete, Post.
	*   Entity GUID :- Get, Delete, PUT
	*   Entity : - Post

* [Relationship operations](http://atlas.apache.org/api/v2/resource_RelationshipREST.html). As on today, below operations are supported for relationships
	*  Relationship :- Post, Put
	*  Relationship GUID : - Delete, Get

* [Search operations](http://atlas.apache.org/api/v2/resource_DiscoveryREST.html). As on today, below operations are supported for search in Atlas
	*  Search : - Get
	
* [TypeDefs operations](http://atlas.apache.org/api/v2/resource_TypesREST.html). As on today, below operations are supported for TypeDefs
	*  Search : - Get, Delete, Post, Put

API Wrapper is using file based authentication mechanism to connect with Atlas, same is used for basic Authorization while accessing the APIs . For more information, see [Authentication & Authorization in Apache Atlas](https://atlas.apache.org/0.8.1/Authentication-Authorization.html).

## Using the API Wrapper

The APIs documented in this section provide access to operations on Atlas data, such as entities creation and population, TypeDefs upload, and queries. When calling APIs, keep the following points in mind:

* All APIs will be issued over HTTPS (on the default port 8080).

* You can use Swagger-ui.html to get APIs details.

More details coming soon

## This library is built using:

* JDK / JRE 1.8
* Spring 2.0
* Junit 4.12

## Building the SDK

1. Clone this repo 
2. In [Eclipse](https://www.eclipse.org/downloads/), import the project importing the folder - it will open the project and will make sure all dependencies are met..
 More details coming soon

## How to provide feedback

See our [Contribution Guidelines](./.github/CONTRIBUTING.md).

## How to get support
See our [Support Guidelines](./.github/SUPPORT.md)

## Known issues

TBD

## FAQ

### How to run unit tests

TBD

## Contributing
If you would like to become an active contributor to this project please follow the instructions provided in [Microsoft Azure Projects Contribution Guidelines](http://azure.github.io/guidelines.html).

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Run style check locally
TBD