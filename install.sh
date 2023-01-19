cp main.go oniongen.go
go build oniongen.go
chmod +x oniongen
mv oniongen /bin/
cd
oniongen
