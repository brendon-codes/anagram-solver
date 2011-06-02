
def:
	@echo "Targets: test"

test:
	@./test.py

export:
	rm -fr ../export/anagram/
	mkdir -p ../export/
	git checkout-index -a -f --prefix=../export/anagram/
