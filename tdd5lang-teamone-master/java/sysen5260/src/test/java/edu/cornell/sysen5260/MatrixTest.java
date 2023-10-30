package edu.cornell.sysen5260;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.io.IOException;

import org.junit.Test;

import com.opencsv.exceptions.CsvException;

/**
 * Unit test for simple App.
 */
public class MatrixTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void ctorShouldWork()
    {
        Matrix m = new Matrix(2,2);
        assertTrue( m != null);
    }

    @Test
    public void readCsvShouldReturnCorrectlyPopulatedMatrix() throws IOException, CsvException
    {
        Matrix m = Matrix.readFromCsvFile("/opt/data/mat_a.csv");
        assertTrue(m.nRows==2);
        assertTrue(m.nCols==2);
        assertTrue(m.get(0, 0)==1.0);
        assertTrue(m.get(0, 1)==3.0);
        assertTrue(m.get(1, 0)==2.0);
        assertTrue(m.get(1, 1)==4.0);
    }

    @Test
    public void readWriteReadRountripShouldProduceEquivalentMatrices() throws IOException, CsvException{
        Matrix m = Matrix.readFromCsvFile("/opt/data/mat_a.csv");
        Matrix.writeToCsvFile(m, "/tmp/test-matrix.csv");
        Matrix m2 = Matrix.readFromCsvFile("/tmp/test-matrix.csv");
        assertEquals(m, m2);
    }

    @Test
    public void A_Multiply_BShouldEqual_C() throws IOException, CsvException{
        Matrix a = Matrix.readFromCsvFile("/opt/data/mat_a.csv");
        Matrix b = Matrix.readFromCsvFile("/opt/data/mat_b.csv");
        Matrix expected = Matrix.readFromCsvFile("/opt/data/mat_c.csv");
        Matrix actual = a.multiply(b);
        assertEquals("a.multiply(b) doesn't match expected matrix", expected, actual);
    }


    // Test if the matrix multiplication throws an exception when the dimensions are incompatible
    @Test(expected = IllegalArgumentException.class)
    public void multiplicationOfCompatibleMatricesShouldNotThrowException() throws IOException, CsvException{
    Matrix d = Matrix.readFromCsvFile("/opt/data/mat_d.csv"); // 2x4
    Matrix a = Matrix.readFromCsvFile("/opt/data/mat_a.csv"); // 2x2
    d.multiply(a); // This should throw an exception
}

    // Test multiply an NxM matrix with an MxP matrix and get back the NxP matrix product
    @Test
    public void D_Multiply_EShouldEqual_F() throws IOException, CsvException{
        Matrix d = Matrix.readFromCsvFile("/opt/data/mat_d.csv");
        Matrix e = Matrix.readFromCsvFile("/opt/data/mat_e.csv");
        Matrix expected = Matrix.readFromCsvFile("/opt/data/mat_f.csv");
        Matrix actual = d.multiply(e);
        assertEquals("d.multiply(e) doesn't match expected matrix", expected, actual);
    }

}
