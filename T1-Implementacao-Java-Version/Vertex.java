import java.util.HashSet;
import java.util.Set;

public class Vertex {

	private Set<Vertex> neighbours;

	public Vertex() {
		this.neighbours = new HashSet<Vertex>();
	}

	public int degree() {
		return this.neighbours.size();
	}

	public Set<Vertex> get_neighbours() {
		return neighbours;
	}

	public boolean is_neighbours(Vertex v) {
		return this.neighbours.contains(v);
	}
}
