package citydatabase;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;

/**
 * This Class holds some Utils functions used across the project.
 */
public class Utils {

	/**
	 * Util function to count how many lines a file has.
	 * 
	 * Maybe not too efficient, but we will only need this
	 * once, so this should be fine.
	 * RT: Theta(n)
	 * @param filepath
	 * @return
	 * @throws IOException
	 */
	public static int countLines(BufferedReader br) throws IOException {
		int lines = 0;
		while (br.readLine() != null) {
			lines++;
		}
		return lines;
	}
	
	/**
	 * Takes a line (hopefully a cities db line!), splits it
	 * by \t (tabulator) and returns an Object[]
	 * where the first and second elements are strings
	 * (city and country), third is a integer (population)
	 * fourth and fifth are gps coordinates.
	 * @param line
	 * @return
	 */
	public static Object[] parseCitiesLine(String line) {
		// Split line by tab
		String[] splittedLine = line.split("\\t");
		Object[] parsedLine = new Object[5];
		parsedLine[0] = splittedLine[0];
		parsedLine[1] = splittedLine[1];
		parsedLine[2] = Integer.parseInt(splittedLine[2]);
		parsedLine[3] = Float.parseFloat(splittedLine[3]);
		parsedLine[4] = Float.parseFloat(splittedLine[4]);
		
		return parsedLine;
	}

	/**
	 * Sorts a LinkedList (found) containing city Objects by population.
	 * Mutates found. First element will be city with highest population.
	 * 
	 * @param found
	 */
	public static void sortByPopulation(LinkedList<Object[]> found) {
		// Because population is inside object[], we need a custom
		// comparator, getting and casting population (2nd index).
		Collections.sort(found, new Comparator<Object[]>() {
			@Override
			public int compare(Object[] o1, Object[] o2) {
				return (int) o2[2] - (int) o1[2];
			}
		});
		
	}
	
	/**
	 * We want the cities to be sorted with posix locale,
	 * sadly the given cities.txt isn't so force it!
	 * Mutates cities.
	 * @param cities
	 */
	public static void sortCitiesByName(Object[][] cities) {
		Arrays.sort(cities, new Comparator<Object[]>() {
			@Override
			public int compare(Object[] o1, Object[] o2) {
				return ((String) o1[0]).compareTo((String) o2[0]);
			}
		});
	}
}
