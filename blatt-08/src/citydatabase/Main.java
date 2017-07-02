/**
 * Aufgabe 2:
 * 
 * Meiner Meinung nach macht es am meisten Sinn, für die cities datenbank
 * intern ein Feld fester Größe zu benutzen. Die Vorteile liegen hierbei
 * daran, dass wir für jeden insert nur O(1) benötigen (wie mit linkedlists
 * und trees auch), und auch nicht
 * reallozieren müssen, da wir schon zuvor wissen, wieviele cities hinein
 * müssen (anzahl der zeilen). Desweiteren verbrauchen wir weniger Platz
 * als mit linked lists oder trees (müssen kein prev/next/first/last speichern bzw
 * die child nodes) und zusätzlich können wir auch die blockoperationen optimieren,
 * da wir (hoffentlich, wer weiß wie jvm das macht) im speicher nahe aneinander liegen.
 * 
 * 
 * Auch für die prefix suche bietet sich ein feld fester größe an, da wir
 * binary search anwenden können. Dies würde bei Linked lists nicht gehen, bei trees
 * schon.
 * 
 * Desweiteren sortiere ich zu beginn die cities noch einmal nach dem namen, da ansonsten
 * die binäre suche nicht ausreichend gut funktioniert hat (die sortierung ist en_US.utf8,
 * die binäre suche hat aber damit ein problem, wenn zwischen zwei Städten mit U eine Stadt mit 
 * Ü auftaucht.). Wir machen dies einmal, sollte also verkraftbar sein.
 * 
 * Laufzeit:
 * Daten einlesen:
 * Zeilen zählen, in array einfügen, sortieren
 * O(2n + n*log(n)) = O(n*log(n)) 
 * 
 * Präfix Suche:
 * Erste Stadt finden, weitere Städte finden, sortieren
 * O(log(n) + n-1 + n*log(n)) = O(n*log(n))
 */

package citydatabase;

import java.util.Scanner;

/**
 * Main Class.
 * Runs a CLI tool which reads in hardcoded database file
 * and you can perform prefix search over stdin forever.
 * 
 */
public class Main {

	/**
	 * See class description.
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		// Init Database
		Database db = new Database("cities.txt");
		System.out.println("Imported " + db.cities.length + " cities.");

		Scanner sc = new Scanner(System.in);

		String prefix;
		Object[][] cities;
		while (sc.hasNextLine()) {
			prefix = sc.nextLine();
			cities = db.searchByPrefix(prefix);
			if (cities == null) {
				System.out.println("No cities found");
			} else {
				for (Object[] city: cities) {
					System.out.println(
						city[0] + " " + city[1] + " " + city[2] + " " + city[3] + " " + city[4]
					); 
				}				
			}
		}
		
		sc.close();
	}	
}