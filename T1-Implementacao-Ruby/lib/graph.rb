require 'set'
require 'vertex'

class Graph
  attr_accessor :vertices

  def initialize
    @vertices = Set.new
  end

  def add_vertex(vertex)
    self.vertices.add(vertex)
  end

  def connect_vertices(vertex1, vertex2)
    vertex1.neighbours.add(vertex2)
    vertex2.neighbours.add(vertex1)
  end

  def disconnect_vertices(vertex1, vertex2)
    vertex1.neighbours.delete(vertex2)
    vertex2.neighbours.delete(vertex1)
  end

  def disconnect_all_vertices(vertex)
    vertex.neighbours.each do |neighbour|
      self.disconnect_vertices(vertex, neighbour)
    end
  end

  def remove_vertex(vertex)
    self.disconnect_all_vertices(vertex)
    self.vertices.delete(vertex)
  end

  def order
    self.vertices.size
  end

  def depth_first_search(vertex, visited, data)
    unless visited.include?(vertex)
      if vertex.check_data(data)
        vertex
      else
        visited.add(vertex)
        vertex.neighbours.each do |neighbour|
          self.depth_first_search(neighbour, visited, data)
        end
      end
    end
  end

  def select_random_vertex
    self.vertices.to_a.sample
  end
end
