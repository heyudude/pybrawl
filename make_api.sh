rm -rf pybrawl/models
rm -rf docs
rm -rf test
openapi-generator generate -i ../brawlstars-swagger/bs_swagger.yaml -g python --skip-validate-spec --package-name pybrawl -o .
#java -jar swagger-codegen-cli.jar generate -i ../brawlstars-swagger/bs_swagger.yaml --api-package pybrawl --lang python -o .
cat templates/README_suffix.md >> README.md
