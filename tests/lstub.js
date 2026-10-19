(function(){
function B(){ this.ok=true; } B.prototype.isValid=function(){return true}; B.prototype.extend=function(){return this};
function Layer(){ this._l=[]; }
var proto={addTo:function(m){return this},on:function(){return this},bindPopup:function(){return this},addLayer:function(l){this._l.push(l);return this},
 eachLayer:function(f){this._l.forEach(f);return this},getLayers:function(){return this._l},getBounds:function(){return new B()},
 fitBounds:function(){return this},setView:function(){return this},remove:function(){return this},removeLayer:function(){return this},invalidateSize:function(){return this},setOpacity:function(o){this._op=o;return this},off:function(){return this}};
Object.assign(Layer.prototype,proto);
function mk(){ return new Layer(); }
window.L={map:function(id){var el=document.getElementById(id); el.style.background='repeating-linear-gradient(45deg,#dfe6ec 0 12px,#e8eef3 12px 24px)'; var m=mk(); return m;},
 tileLayer:mk,marker:function(){return mk()},polyline:function(){return mk()},featureGroup:function(){return mk()},divIcon:function(o){return o}};
})();
