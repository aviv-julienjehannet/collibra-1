# Generate collibra-core Python package
This is a client Python package which interacts with Collibra Data Governance cloud platform. The package is generated
based off of instructions of [Create your own Collibra REST API client] tutorial which at high level uses
[OpenApi Generator - for Python].
While the above tutorial is general, following steps highlight how we have used exactly to generate this Python package
on a **MacOS** using the OpenAPI Generator CLI:

## Install OpenAPI Generator CLI on MacOS ##

1. Install [Homebrew]

2. Install _npm_

```sh
brew install node
npm install -g npx
```

3. Install OpenAPI Generator CLI

```sh
npm install @openapitools/openapi-generator-cli -g
```

## Generate Collibra Python client package ##

1. Make and cd to a directory where package needs to be stored

```sh
mkdir collibra
cd collibra
```

2. Download Collibra REST API JSON (_dgc-rest.json_) specification file. For example, [StreamSets community spec]
one is downloaded as (_streamsets-ci_ user credential are stored in [StreamSets 1Password]):

```sh
wget --user=streamsets-ci --ask-password https://streamsets-cloud-license.collibra.com/docs/restv2/dgc-rest.json
```

3. Generate Collibra Python package as:

```sh
npx @openapitools/openapi-generator-cli generate -g python -i dgc-rest.json -o collibra-core --package-name collibra_core
```

4. Verify, install (or upload to Github) the new Python package

```sh
cd collibra-core
pip3 install -e .
```

## Usage and reference ##

### Usage ###

Assuming [StreamSets Assets] are created on Collibra cloud platform with user _streamsets-ci_ having
_Community Manager_ as its *Responsibilities*, we can use and access the Collibra assets as:

```python
import collibra_core
from collibra_core.api.application_api import ApplicationApi

def create_api_client(url, username, password):
    configuration = collibra_core.Configuration()
    configuration.host = url + "/rest/2.0"
    configuration.username = username
    configuration.password = password
    return collibra_core.ApiClient(configuration)

collibra_url = "https://streamsets-cloud-license.collibra.com"
username = "streamsets-ci"
password = "MASKED"

client = create_api_client(collibra_url, username, password)

# Get platform information
platform_info = ApplicationApi(client).get_info()
print ("Platform version: " + platform_info.version.full_version)
print ("Platform build number: " + platform_info.build_number)
```

### Reference ###

* Refer to [Collibra generated doc](collibra-core/README.md) for Collibra Python API usage and reference.
* Refer to [StreamSets Collibra Community doc] for Java API and REST API reference. Remember the Collibra Python package
we generated above is inferred based on the REST API - so lot of cross reference (e.g., what methods are available for
Assets) can be done.


    [Create your own Collibra REST API client]: <https://developer.collibra.com/developer-tutorials/tut_rest-api-client-create/>
    [OpenApi Generator - for Python]: https://openapi-generator.tech/docs/generators/python
    [Homebrew]: https://brew.sh/
    [StreamSets community spec]: https://streamsets-cloud-license.collibra.com/docs/restv2/dgc-rest.json
    [StreamSets 1Password]: https://start.1password.com/open/i?a=B2QP5WLWZVGLJEFVVMELCNMWA4&h=streamsets.1password.com&i=jk4lobjvmvd5lkk2qsvuzj4qhy&v=k4543lm5jpylsn4u5pjypz3ham
    [StreamSets Assets]: https://streamsets-cloud-license.collibra.com
    [StreamSets Collibra Community doc]: https://streamsets-cloud-license.collibra.com/docs/index.html
