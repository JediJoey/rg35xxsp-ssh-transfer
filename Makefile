.PHONY: clean build

clean:
	sudo rm -rf build
	sudo rm -rf dist
	sudo rm -rf rg35xxsp_ssh_transfer.egg-info/

build:
	pip uninstall rg35xxsp-ssh-transfer -y || true
	python setup.py sdist bdist_wheel
	pip install dist/*.whl
	make clean
