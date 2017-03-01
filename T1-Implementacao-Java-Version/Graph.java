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
		int rand_degree = this.get_random_vertex().degree();
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
	
	public Set<Vertex> transitive_closure(Vertex v) {
		return this.search_for_transitive_closure(v, (new HashSet<Vertex>()));
	}
	
	public Set<Vertex> search_for_transitive_closure(Vertex v, Set<Vertex> visited) {
		visited.add(v);
		for (Vertex i: v.get_neighbours()) {
			if (!(visited.contains(i))) {
				search_for_transitive_closure(i, visited);
			}
		}
		return visited;
	}
	
	public boolean is_tree() {
			Vertex v = this.get_random_vertex();
			return (this.is_connected()) && this.has_cycle(v, v, (new HashSet<Vertex>())); 
	}
	
	public boolean is_connected() {
		return this.vertex == this.transitive_closure(this.get_random_vertex());
	}
	
	public boolean has_cycle(Vertex v1, Vertex v2, Set<Vertex> visited) {
		if (visited.contains(v1)) {
			return true;
		}
		
		visited.add(v1);
		for(Vertex i:v1.get_neighbours()) {
			if (i != v2) {
				if (has_cycle(i, v1, visited)) {
					return true;
				}
			}
		}
		visited.remove(v1);
		return false;
	}
}
