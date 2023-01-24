[![Build Status](https://fms01lxuthub01.amr.corp.intel.com/api/badges/ase-internal/PAASclient/status.svg)](https://fms01lxuthub01.amr.corp.intel.com/ase-internal/PAASclient)


## PAASclient
A REST client for PAAS API


#### Usage

Create environment variables - required if not using session token to connect

```bash
export PAAS_API_KEY=<PAAS-API-KEY>
```

NOTE: you may obtain a PAAS API key from the Cloud Services Portal: https://cloudservices.intelcloud.intel.com


```python
# python
>>> from PAASclient import PAASclient

# get production instance of PAASclient
>>> client = PAASclient.get_PAASclient()

# get iap usage data for the past 3 months
>>> client.get_iap_usage(months=3)
```


#### Docker Usage

To run with Docker, first build the image. The `-t` flag indicates the name of the Docker image, which must be all lowercase. You must navigate to the same directory as `Dockerfile` (which is the root directory in this case):

```bash
docker build -t paasclient:latest .
```

Note that you can change `latest` to be whatever you want, so long as it follows appropriate valid naming conventions for docker image tags.

Then, run the image, taking into consideration the proper environment variables - make sure to change them!

```bash
 docker run --rm \
--env PAAS_API_KEY=<PAAS-API-KEY> \
-it paasclient:latest \
python
```

The above command will bring up a python interpreter, with `PAASclient` ready to be imported as shown in this readme. Additionally, to avoid keeping the key in bash history, a space has been prepended to the above command.

You can use Docker volume mounts to run a specific script that you've coded locally, but have not actually installed PAASclient. Do it like this:

```bash
 docker run --rm \
-v /path/to/your/python_file.py:/python_file.py \
--env PAAS_API_KEY=<PAAS-API-KEY> \
-it paasclient:latest \
python /python_file.py
```
