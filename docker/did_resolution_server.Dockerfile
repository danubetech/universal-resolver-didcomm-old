# Dockerfile for universalresolver/universal-resolver-didcomm

FROM bcgovimages/von-image:py36-1.15-0

ENV ENABLE_PTVSD 0

RUN mkdir bin && curl -L -o bin/jq \
	https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 && \
	chmod ug+x bin/jq

# Add and install Indy Agent code
ADD requirements*.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

ADD aries_cloudagent ./aries_cloudagent
ADD bin ./bin
ADD README.md ./
ADD scripts ./scripts
ADD setup.py ./

RUN pip3 install --no-cache-dir -e .

RUN mkdir logs && chown -R indy:indy logs && chmod -R ug+rw logs

ENV public_endpoint_http=http://dev.uniresolver.io:8180
ENV public_endpoint_ws=ws://dev.uniresolver.io:8181
ENV did_resolution_service=https://dev.uniresolver.io/1.0/identifiers/{did}


EXPOSE 8180 8181

ENTRYPOINT ["/bin/bash", "-c", "aca-py start -it http 0.0.0.0 8180 -it ws 0.0.0.0 8181 -ot http -ot ws --auto-accept-invites --auto-accept-requests --endpoint $public_endpoint_ws --endpoint $public_endpoint_http --auto-respond-messages --label did-resolution --did-resolution-service $did_resolution_service --public-invite --invite --invite-multi-use --no-ledger --emit-new-didcomm-prefix"]
