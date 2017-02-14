import java.util.HashSet;
import java.util.Random;
import java.util.Set;


public class Graph {

	private Set<Vertex> vertex;
	
	public Graph() {
		this.vertex = new HashSet<Vertex>();
	}
	
	public void add_vertex(Vertex v) {
		this.vertex.add(v);
	}
	
	public void remove_vertex(Vertex v) {
		for (Vertex i:v.get_neighbours()) {
			this.disconnect(v, i);
		}
		this.vertex.remove(v);
	}
	
	public void connect(Vertex v1, Vertex v2) {
		v1.get_neighbours().add(v2);
		v2.get_neighbours().add(v1);
	}
	
	public void disconnect(Vertex v1, Vertex v2) {
		v1.get_neighbours().remove(v2);
		v1.get_neighbours().remove(v1);
	}
	
	public int order() {
		return this.vertex.size();
	}
	
	public Set<Vertex> get_vertex() {
		return this.vertex;
	}
	
	public Vertex get_random_vertex() {
		Vertex[] vertex_array = (Vertex[])this.vertex.toArray();
		int rand = (new Random()).nextInt((vertex_array.length));
		return vertex_array[rand];
	}
	
	public Set<Vertex> adjacent(Vertex v) {
		return v.get_neighbours();
	}
	
	public int degree(Vertex v) {
		return v.degree();
	}
	
	public boolean is_regular() {
		int rand_degree = get_random_vertex().degree();
		for(Vertex i: this.vertex) {
			if (i.degree() != rand_degree) {
				return false;
			}
		}
		return true;
	}
	
	public boolean is_complete() {
		for(Vertex i: this.vertex) {
			for(Vertex j: this.vertex) {
				if (!(i.is_neighbours(j))) {
					return false;
				}
			}
		}
		return true;
	}
	
	public Set<Vertex> transitive_closure(Vertex v, Set<Vertex> visited) {
		visited.add(v);
		for(Vertex i:v.get_neighbours()) {
			if (!(visited.contains(i))) {
				transitive_closure(i, visited);				
			}
		}
		return visited;
	}
}
