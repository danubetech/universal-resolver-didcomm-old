This is the Universal Resolver DIDComm agent interface, based on ACA-Py (see https://github.com/hyperledger/aries-cloudagent-python/).

# Overview

The DIDComm agent in this repository can be used both as a Universal Resolver DIDComm agent, and as a client DIDComm agent that connects to it and sends DID resolution requests.

The Universal Resolver DIDComm agent generates a connection invitation that can be used by client DIDComm agents.

Both agents are marked in red in the following diagram:

![architecture-agents](https://raw.githubusercontent.com/danubetech/universal-resolver-didcomm/main/diagrams/architecture-agents.png)

# Building

Building locally with Python:

```
# install (debian) packages, pip and virtualenv:
sudo apt install python3-virtualenv python3-pip
# or alternatively: pip install virtualenv
# install aries-cloudagent including the did resolution protocol
mkdir venv
virtualenv -p python3 venv/
source venv/bin/activate
pip install -r requirements.txt
git clone git@github.com:danubetech/universal-resolver-didcomm.git
cd universal-resolver-didcomm
git checkout main
pip install --no-cache-dir -e .
pip install python3-indy
```

Building a Docker image:

`docker build . -f docker/did_resolution_demo.Dockerfile -t universalresolver/universal-resolver-didcomm-demo:latest`

# Starting the Universal Resolver DIDComm agent

Locally using Python:

```
aca-py start -it http 127.0.0.1 3555 -ot http --auto-accept-invites --auto-accept-requests --endpoint http://127.0.0.1:3555 --auto-respond-messages --label Server --log-level debug --public-invite --invite --invite-base-url http://localhost:3555 --invite-multi-use --no-ledger --admin-insecure-mode --admin 127.0.0.1 3000 --write-invitation-to=~/didcomm-invitation.txt --emit-new-didcomm-prefix
```

Using Docker:

```
docker run --net=host -p 3000:3000 -p 3555:3555 -i -t universalresolver/universal-resolver-didcomm-demo:latest start --admin-insecure-mode --admin 0.0.0.0 3000 -it http 0.0.0.0 3555 -ot http --auto-accept-invites --auto-accept-requests --endpoint http://127.0.0.1:3555 --auto-respond-messages --label Server --log-level debug  --public-invite --invite --invite-base-url http://localhost:8080 --no-ledger --emit-new-didcomm-prefix
```

# Starting the client DIDComm agent

Locally using Python:

```
aca-py start --admin-insecure-mode --admin 127.0.0.1 4000 -it http 127.0.0.1 4555 -ot http --auto-accept-invites --auto-accept-requests --endpoint http://127.0.0.1:4555 --auto-store-credential --auto-respond-messages --label Client --auto-ping-connection --log-level debug --no-ledger --emit-new-didcomm-prefix
```

Using Docker:

```
docker run --net=host -p 4000:4000 -p 4555:4555 -i -t universalresolver/universal-resolver-didcomm-demo:latest start --admin-insecure-mode --admin 0.0.0.0 4000 -it http 0.0.0.0 4555 -ot http --auto-accept-invites --auto-accept-requests --endpoint http://127.0.0.1:4555 --auto-store-credential --auto-respond-messages --label Client --auto-ping-connection --log-level debug --no-ledger --emit-new-didcomm-prefix
```

# Websocket demo

Starting the Universal Resolver DIDComm agent:

```
aca-py start -it ws 127.0.0.1 3555 -ot ws --auto-accept-invites --auto-accept-requests --endpoint ws://127.0.0.1:3555 --auto-respond-messages --label Server --log-level debug --public-invite --invite --invite-base-url ws://localhost:3555 --invite-multi-use --no-ledger --admin-insecure-mode --admin 127.0.0.1 3000 --write-invitation-to=/home/fonfon/code/danubetech/did-resolution-demo/invitation.txt --no-ledger --emit-new-didcomm-prefix
```

Starting the client DIDComm agent:

```
aca-py start --admin-insecure-mode --admin 127.0.0.1 4000 -it ws 127.0.0.1 4555 -ot ws --auto-accept-invites --auto-accept-requests --endpoint ws://127.0.0.1:4555 --auto-store-credential --auto-respond-messages --label Client --auto-ping-connection --log-level debug --no-ledger --emit-new-didcomm-prefix
```

# Websocket demo with hard-coded seed / invitation

Not yet working; start server without --invite-multi-use but with --invite-public:

Starting the Universal Resolver DIDComm agent:

```
aca-py start -it ws 127.0.0.1 3555 -ot ws --auto-accept-invites --auto-accept-requests --endpoint ws://127.0.0.1:3555 --auto-respond-messages --label Server --log-level debug --public-invite --invite --public-invites --invite-public --invite-base-url ws://localhost:3555 --seed 12345678912345678912345678912345 --emit-new-didcomm-prefix
```

Starting the client DIDComm agent:

```
aca-py start --admin-insecure-mode --admin 127.0.0.1 4000 -it ws 127.0.0.1 4555 -ot ws --auto-accept-invites --auto-accept-requests --endpoint ws://127.0.0.1:4555 --auto-store-credential --auto-respond-messages --label Client --auto-ping-connection --log-level debug --emit-new-didcomm-prefix
```
