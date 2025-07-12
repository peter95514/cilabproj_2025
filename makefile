#makefile

init:
	@echo "creating vitural environment..."
	bash scripts/init_venv.sh

clean:
	@echo "cleaning vitural environment"
	rm -rf venv 
