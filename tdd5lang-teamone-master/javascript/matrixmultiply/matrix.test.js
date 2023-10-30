const matrix = require('./matrix.js');

test('mpy mat-a * mat-b should yield mat-c.', () => {
	let matA = matrix.readMatrix('../data/mat_a.csv');
	expect(matrix.matmpy(1, 2)).toBe(3);
});

test('read-write-read roundtrip should be equal.', () => {
	let matA = matrix.readMatrix('../data/mat_a.csv');
	matrix.writeMatrix(matA, '/tmp/test-matrix.csv');
	let matB = matrix.readMatrix('/tmp/test-matrix.csv');
	expect(matA).toEqual(matB);
});

test('matrix.multiply should produce acorrect result.', () => {
	let matA = matrix.readMatrix('../data/mat_a.csv');
	let matB = matrix.readMatrix('../data/mat_b.csv');
	let expected = matrix.readMatrix('../data/mat_c.csv');
	let actual = matrix.multiply(matA, matB);
	expect(actual).toEqual(expected);
});

test('matrix.multiply should throw an error if the matrices cannot be multiplied.', () => {
	// A 2x2 matrix
	let matA = matrix.readMatrix('../data/mat_a.csv');
	// A 2x3 matrix
	let matB = matrix.readMatrix('../data/mat_d.csv');

	expect(() => matrix.multiply(matA, matB)).toThrow(
		'Matrices cannot be multiplied',
	);
});

test('matrix.multiply should be able to multiply an NxM matrix with an MxP matrix and get back the NxP matrix product', () => {
	// A 2x2 matrix
	let matA = matrix.readMatrix('../data/mat_a.csv');
	// A 2x1 matrix
	let matB = matrix.readMatrix('../data/mat_f.csv');
	let expected = matrix.readMatrix('../data/mat_g.csv');
	let actual = matrix.multiply(matA, matB);
	expect(actual).toEqual(expected);
});

test('readMatrix should ignore empty lines.', () => {
	let matA = matrix.readMatrix('../data/mat_e.csv');
	let expected = matrix.readMatrix('../data/mat_a.csv');
	expect(matA).toEqual(expected);
});

test('readMatrix should throw an error if the file does not exist.', () => {
	expect(() => matrix.readMatrix('../data/mat_z.csv')).toThrow(
		"ENOENT: no such file or directory, open '../data/mat_z.csv'",
	);
});
