.PHONY: test, clean

matmpy: matmpy.c
	gcc -g matmpy.c -o matmpy

result.csv: ./matmpy
	./matmpy /opt/data/mat_a.csv /opt/data/mat_b.csv > result.csv

expected.csv: /opt/data/mat_c.csv
	cp /opt/data/mat_c.csv expected.csv
	dos2unix expected.csv	

test1_result.csv: ./matmpy
	./matmpy /opt/data/test1_mat_a.csv /opt/data/test1_mat_b.csv > test1_result.csv

test1_expected.csv: /opt/data/test1_mat_c.csv
	cp /opt/data/test1_mat_c.csv test1_expected.csv
	dos2unix test1_expected.csv	

test2_result.csv: ./matmpy
	./matmpy /opt/data/test2_mat_a.csv /opt/data/test2_mat_b.csv > test2_result.csv

test2_expected.csv: /opt/data/test2_mat_c.csv
	cp /opt/data/test2_mat_c.csv test2_expected.csv
	dos2unix test2_expected.csv	

test: result.csv expected.csv test1_result.csv test1_expected.csv test2_result.csv test2_expected.csv
	diff expected.csv result.csv
	@echo "PASS"
	diff test1_expected.csv test1_result.csv
	@echo "PASS test1 for different dimensions"
	diff test2_expected.csv test2_result.csv
	@echo "PASS test2 for incomptable dimensions"

clean:
	rm -f *.o matmpy result.csv expected.csv
