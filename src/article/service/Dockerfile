FROM golang:1.20

WORKDIR /app

COPY go.mod ./

RUN go mod download

COPY *.go ./

RUN go build -o /docker-article-svc

CMD ["/docker-article-svc"]
